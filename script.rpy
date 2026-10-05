init python:

    class CharacterStats(BaseStatsObject):

        STAT_DEFAULTS = {
            'name' : 'Daisy',
            'age' : 31,
            'weight' : 52.0,
            'leanweight' : 40.2,
            'characterheight' : 161,
            'characterheightimperial' : '5′3″',
            'breast_weight' : 0.8,
            'breast_cup' : '32D',
            'breast_size' : 36.2,
            'waist_size' : 23.1,
            'ass_size' : 36.1,
            'stage' : 1,
            'hunger' : 1,
            'stomach_capacity' : 1.6,
            'fullness' : 0.0,
            'lactation' : 0,
            'addiction_to_food' : 1.0,
            'stage' : 1,
            'maxstage' : 17,
            'type' : 'apple',
        }

    def PopulateEvents(girl):
        global events
        possibleEvents = []
        girlName = str.lower(girl.name)
        if girlName == "daisy":
            girlName = "teacher"
        elif girlName == "lyn":
            girlName = "leanne"
        for x in renpy.get_all_labels():
            if str.lower(x).startswith(girlName) and "event" in str.lower(x):
                possibleEvents += [x]
        for x in possibleEvents:
            if str.lower(x).endswith("1"):
                if globals()[(str.lower(x).replace("_",""))[:-1]] == 0:
                    events += [x]
            elif globals()[(str.lower(x).replace("_",""))] == 0:
                events += [x]
        events.sort(key=EventStage)
        return

    def EventStage(event):
        girlName = selectedCharacter.name
        if girlName == "Daisy":
            girlName = "Teacher"
        if girlName == "Lyn":
            girlName = "Leanne"
        event = event.replace(girlName + "_Stage_","")
        if event[-1].isdigit():
            tempflt = float(event[-1])
            event = event[:-8]
            return float(event) + (tempflt / 10)
        else:
            event = event[:-6]
            return float(event)

    def ClearEvents():
        global events
        events.clear()
        return

    def AppendGirls():
        import math
        global availableGirls, galMaxPage
        availableGirls.append(teacher)
        if luna_stats_visible == 1:
            availableGirls.append(luna)
        if leanne_stats_visible == 1:
            availableGirls.append(leanne)
        if katrine_stats_visible == 1:
            availableGirls.append(katrine)
        if marie_stats_visible == 1:
            availableGirls.append(marie)
        if lisa_stats_visible == 1:
            availableGirls.append(lisa)
        if amber_stats_visible == 1:
            availableGirls.append(amber)
        if maya_stats_visible == 1:
            availableGirls.append(maya)
        if cayenne_stats_visible == 1:
            availableGirls.append(cayenne)
        if caroline_stats_visible == 1:
            availableGirls.append(caroline)
        if vicky_stats_visible == 1:
            availableGirls.append(vicky)
        if sallystage3event == 0:
            availableGirls.append(sally)
        #if mylenna_stats_visible == 1:
        #    availableGirls.append(mylenna)
        if bonnie_stats_visible == 1:
            availableGirls.append(bonnie)
        if rebecca_stats_visible == 1:
            availableGirls.append(rebecca)
        if trista_stats_visible == 1:
            availableGirls.append(trista)
        if hari_stats_visible == 1:
            availableGirls.append(hari)
        if nataliestage3event == 0:
            availableGirls.append(natalie)
        if brittastage4event == 0:
            availableGirls.append(britta)
        if roxiestage4event == 0:
            availableGirls.append(roxie)
        availableGirls.sort(key=getName)
        galMaxPage = int(math.ceil((len(availableGirls) / 3) - 1))
        return

    def getName(girlobj):
        return girlobj.name


init:
    $ name = u'[playername]' # default your name
define nm = DynamicCharacter("pc") # your character

#Main Characters
define pc = Character(_("[playername]"), color="#9dace3")
define character.teacher = Character("Daisy")
define character.luna = Character("Luna")
define character.leanne = Character("[Lynname]", color="#c52896")
define character.katrine = Character("Katrine")
define character.marie = Character("Marie")
define character.lisa = Character("Lisa")
define character.amber = Character("Amber")
define character.cayenne = Character("Cayenne")
define character.trista = Character("Trista")
define character.bonnie = Character("Bonnie")
define character.caroline = Character("Caroline")
define character.maya = Character("Maya")
define character.hari = Character("Hari")
define character.vicky = Character("Vicky")
define character.roxie = Character("Roxie")
define character.natalie = Character("Natalie")
define character.charlene = Character("Charlene")
define character.sally = Character("Sally")
define character.britta = Character("Britta")
define character.mylenna = Character("Mylenna")
define character.rebecca = Character("Rebecca")
default teacher = CharacterStats("teacher", age=31, location='University')
default marie = CharacterStats("marie", name='Marie', age=26, weight=60.0, characterheight=173, characterheightimperial='5′8″', breast_weight=0.6, breast_cup='30B', breast_size=32.2, waist_size=24.6, ass_size=37.5, maxstage=11, type='apple', leanweight=51.1)
default luna = CharacterStats("luna", name='Luna', age=29, weight=54.0, characterheight=161, characterheightimperial='5′3″', breast_weight=1.1, breast_cup='32D', breast_size=36.3, waist_size=23.4, ass_size=36.3, stomach_capacity=1.2, maxstage=12, type='hourglass', leanweight=43.1)
default leanne = CharacterStats("leanne", name='Leanne', age=22, weight=53.0, characterheight=175, characterheightimperial='5′9″', breast_weight=0.7, breast_cup='30C', breast_size=34.2, waist_size=23.9, ass_size=35.1, stomach_capacity=1, maxstage=15, type='hourglass', leanweight=46.7)
default katrine = CharacterStats("katrine", name='Katrine', age=34, weight=80.0, characterheight=172, characterheightimperial='5′8″', breast_weight=1.0, breast_cup='34F', breast_size=40.1, waist_size=29.1, ass_size=43.7, stomach_capacity=2, maxstage=11, type='pear', leanweight=62.8)
default lisa = CharacterStats("lisa", name='Lisa', age=28, weight=54.0, characterheight=155, characterheightimperial='5′1″', breast_weight=1.0, breast_cup='34D', breast_size=38.0, waist_size=24.6, ass_size=34.9, stomach_capacity=1, maxstage=12, type='hourglass', leanweight=41.1)
default amber = CharacterStats("amber", name='Amber', age=24, weight=50.0, characterheight=154, characterheightimperial='5′1″', breast_weight=0.8, breast_cup='30C', breast_size=33.6, waist_size=25.2, ass_size=35.2, stomach_capacity=1.2, maxstage=13, type='apple', leanweight=40.8)
default cayenne = CharacterStats("cayenne", name='Cayenne', age=25, weight=50.0, characterheight=167, characterheightimperial='5′6″', breast_weight=0.9, breast_cup='32D', breast_size=36.2, waist_size=24.8, ass_size=35.2, stomach_capacity=1.0, maxstage=11, type='hourglass', leanweight=43.5)
default trista = CharacterStats("trista", name='Trista', age=28, weight=78.0, characterheight=172, characterheightimperial='5′8″', breast_cup='32D', breast_size=35.7, waist_size=24.6, ass_size=42.7, stomach_capacity=1.4, maxstage=13, type='pear', leanweight=66.5)
default bonnie = CharacterStats("bonnie", name='Bonnie', age=26, weight=70.0, characterheight=170, characterheightimperial='5′7″', breast_cup='32D', breast_size=36.2, waist_size=25.0, ass_size=42.8, stomach_capacity=1.3, maxstage=13, type='pear', leanweight=50.2)
default hari = CharacterStats("hari", name='Hari', age=22, weight=47.0, characterheight=157, characterheightimperial='5′2″', breast_cup='28B', breast_size=30.1, waist_size=22.6, ass_size=41.3, maxstage=8, type='pear', leanweight=41.0)
default vicky = CharacterStats("vicky", name='Vicky', age=23, weight=92.0, characterheight=209, characterheightimperial='6′10″', breast_cup='34E', breast_size=39.8, waist_size=26.9, ass_size=43.6, maxstage=5, type='hourglass', leanweight=74.0)
default caroline = CharacterStats("caroline", name='Caroline', age=21, weight=76.0, characterheight=180, characterheightimperial='5′11″', breast_cup='32C', breast_size=35.3, waist_size=24.8, ass_size=39.0, maxstage=4, type='hourglass', leanweight=61.2)
default maya = CharacterStats("maya", name='Maya', age=32, weight=77.0, characterheight=179, characterheightimperial='5′10″', breast_weight=1.9, breast_cup='34G', breast_size=41.0, waist_size=24.7, ass_size=40.3, maxstage=11, type='hourglass', leanweight=59.6)
default roxie = CharacterStats("roxie", name='Roxie', age=26, weight=61.0, characterheight=170, characterheightimperial='5′7″', breast_weight=0.7, breast_cup='30D', breast_size=33.8, waist_size=22.2, ass_size=37.1, maxstage=4, type='strawberry', leanweight=48.3)
default natalie = CharacterStats("natalie", name='Natalie', age=29, weight=64.0, characterheight=171, characterheightimperial='5′7″', breast_weight=0.55, breast_cup='30C', breast_size=32.9, waist_size=23.9, ass_size=41.5, maxstage=4, type='strawberry', leanweight=48.5)
default charlene = CharacterStats("charlene", name='Charlene', age=33, weight=78.0, characterheight=175, characterheightimperial='5′9″', breast_weight=1.0, breast_cup='32E', breast_size=37.2, waist_size=26.2, ass_size=38.8, maxstage=4, type='apple', leanweight=54.1)
default sally = CharacterStats("sally", name='Sally', age=38, weight=74.0, characterheight=175, characterheightimperial='5′9″', breast_weight=0.88, breast_cup='32D', breast_size=35.6, waist_size=25.7, ass_size=39.7, maxstage=4, type='pear', leanweight=53.2)
default britta = CharacterStats("britta", name='Britta', age=27, weight=68.0, characterheight=171, characterheightimperial='5′7″', breast_weight=0.5, breast_cup='32B', breast_size=34.3, waist_size=27.0, ass_size=41.5, maxstage=4, type='strawberry', leanweight=49.8)
default mylenna = CharacterStats("mylenna", name='Mylenna', age=30, weight=54.0, characterheight=172, characterheightimperial='5′8″', breast_weight=1.9, breast_cup='30E', breast_size=34.8, waist_size=22.8, ass_size=37.2, maxstage=2, type='strawberry', leanweight=48.4)
default rebecca = CharacterStats("rebecca", name='Rebecca', age=26, weight=82.0, characterheight=179, characterheightimperial='5′11″', breast_weight=1.9, breast_cup='34E', breast_size=38.8, waist_size=26.9, ass_size=46.3, maxstage=3, type='hourglass', leanweight=60.0)
default selectedCharacter = teacher

#Side Characters that have stages
define character.librarian = Character("Librarian")
default librarian = CharacterStats("librarian", name='Librarian', age=26, weight=60.0, characterheight=173, characterheightimperial='5′8″', breast_weight=0.6, breast_cup='30B', breast_size=32.2, waist_size=24.6, ass_size=37.5, maxstage=11, type='apple', leanweight=51.1)

#Side Characters
define ms = Character('Male Student', color="#ffc8c8")
define fs = Character('Female Student', color="#c8c8c8")
define s = Character('Students')
define bartender = Character('Bartender')
define announcer = Character('Announcer')
define customer = Character('Customer')
define protesters = Character('Crowd of protesters')
define waitress = Character('Waitress')
define woman = Character('Woman')
define gebi = Character('Gebi')
define vanthorne = Character('Mr. Vanthorne')
define tessa = Character('Tessa')
define gina = Character('Gina')
define rayla = Character('Rayla')
define jaimy = Character('Jaimy')
define mandy = Character('Mandy')
define mira = Character('Mira')
define nuit = Character('Nuit')
define esmeralda = Character('Esmeralda')
define gnn = Character('Gebi and Nuit')
define chloe = Character('Chloe')
define lucy = Character('Lucy')
define hanna = Character('Hanna')
define tracy = Character('Tracy')
define catie = Character('Catie')
define jess = Character('Jess')
define nadia = Character('Nadia')
define person = Character('Another Woman')
define cmum = Character('Caroline’s mum')
define gabe = 'Anime Store Clerk'
define Lynname = 'Leanne'
define unknownname = 'Unknown'
define cook = Character('Cook')
default unknown = Character('[unknownname]')
default admin = Character('Administrator')
default animestore = Character('[gabe]')

default gymSplit = [katrine, trista, lisa, bonnie]

#variables
default fcversion = 12
default keep_working = 0
default phonegirl = 'Daisy'
default viewstage = 1
default turnaround = 0
default undress = False
default outfit = 0
default charselect = 'teacher'
default calories = 0
default day = 1
default day2 = 'Monday'
default time2 = 'Morning'
default week = 1
default daytime = 1 #1=morning 2=afternoon 3=evening/night
default stage = 1
default librarianstage = 1
default strip = 0
default bellyrub = 0
default rng = 0
default rngshowoff = 0
default rngworkgirl = 0
default rnggymcharacter = 0
default lunamorningrng = 0
default leannechoice = 0
default rnggym = 0
default carryweight = 0
default phonecall = 0
default workcall = 0
default stuffed = 0
default mealoption = 1
default final_food_capacity = 0
default actions = 4
default eatcount = 0
default money = 200
default lastfooditem = 0
default foodheld = 0
default charisma = 1
default strength = 1
default knowledge = 1
default storyview = False
default quickmenuvisible = False
default disable = 0

#Variables that reset weekly
default weeklyprize = 1
default nataliemilkcheck = 1
default brittamilkcheck = 1
default hari_study_times = 0
default caroline_study_times = 0
default vicky_study_times = 0

default worked_today = 0 # variable that makes sure you can only work once a day
default bookday = 0 # 0 = weekday after university / 1 = weekend / 2 = weekday during university
default daycount = 0 # variable that counts the days since Leanne her stream got banned
default daycount2 = 0 # variable that counts the days since Hari gets mad at you
default daycount3 = 0 # variable that counts the days since Cayenne stops gaining weight
default daycount4 = 0 # variable that counts the days since Caroline lost her leg.
default daycount5 = 0 # variable that counts the days since Maya got the stripclub back
default events = []
default recollection = False # variable that is set to True if watching back an event so we can make sure it doesn't add weight to the character
default availableGirls = []
default galPage = 0
default galMaxPage = 0

#Checks so that the same girl doesn't come twice as customer at bunny bites
default hari_work_today = 0
default marie_work_today = 0
default lisa_work_today = 0
default amber_work_today = 0
default luna_work_today = 0
default daisy_work_today = 0
default leanne_work_today = 0
default bonnie_work_today = 0
default librarian_work_today = 0
default cayenne_work_today = 0
default maya_work_today = 0
default katrine_work_today = 0
default trista_work_today = 0
default caroline_work_today = 0
default vicky_work_today = 0
default roxie_work_today = 0
default natalie_work_today = 0
default charlene_work_today = 0
default sally_work_today = 0
default britta_work_today = 0
default rebecca_work_today = 0
default mylenna_work_today = 0

#Checks so that the same girl doesn't come twice at the gym
default bonnie_gym_today = 0
default rebecca_gym_today = 0
default maya_gym_today = 0
default cayenne_gym_today = 0
default teacher_gym_today = 0
default lisa_gym_today = 0
default hari_gym_today = 0
default marie_gym_today = 0
default katrine_gym_today = 0
default trista_gym_today = 0
default roxie_gym_today = 0

#event triggers, so we can make sure they only happen once
default work_intro = 0
default introcheck = 1
default librarianmeet = 1
default mayaintroduction = 1
default vickyintro1 = 1
default vickyintro2 = 1
default vickyintro3 = 1
default vickystage1event = 1
default vickystage1event2 = 1
default vickystage1event3 = 1
default vickystage1event4 = 1
default vickystage2event = 1
default carolineintro1 = 1
default carolineintro2 = 1
default carolineintro3 = 1
default carolineintro4 = 1
default carolinestage1event = 1
default carolinestage1event2 = 1
default carolinestage1event3 = 1
default carolinestage1event4 = 1
default carolinestage1event5 = 1
default carolinestage2event = 1
default carolinestage2event2 = 1
default carolinestage2event3 = 1
default carolinestage2event4 = 1
default carolinestage3event = 1
default carolinestage3event2 = 1
default carolinestage3event3 = 1
default carolinestage3event4 = 1
default carolinestage3event5 = 1
default carolinestage3event6 = 1
default carolinestage4event = 1
default carolinestage4event2 = 1
default groupprojectstart = 1
default teacherstage2event = 1
default teacherstage3event = 1
default teacherstage4event = 1
default teacherstage5event = 1
default teacherstage6event = 1
default teacherstage6event2 = 1
default teacherstage7event = 1
default teacherstage8event = 1
default teacherstage9event = 1
default teacherstage9event2 = 1
default teacherstage10event = 1
default teacherstage11event = 1
default teacherstage11event2 = 1
default teacherstage12event = 1
default teacherstage13event = 1
default teacherstage14event = 1
default teacherstage15event = 1
default teacherstage16event = 1
default teacherstage17event = 1
default teacherstage18event = 1
default teacherstage19event = 1
default teacherstage20event = 1
default leannestage1event = 1
default leannestage2event = 1
default leannestage2event2 = 1
default leannestage3event = 1
default leannestage4event = 1
default leannestage4event2 = 1
default leannestage5event = 1
default leannestage5event2 = 1
default leannestage6event = 1
default leannestage6event2 = 1
default leannestage7event = 1
default leannestage7event2 = 1
default leannestage8event = 1
default leannestage8event2 = 1
default leannestage8event3 = 1
default leannestage9event = 1
default leannestage9event2 = 1
default leannestage10event = 1
default leannestage10event2 = 1
default leannestage11event = 1
default leannestage11event2 = 1
default leannestage11event3 = 1
default leannestage11event4 = 1
default leannestage11event5 = 1
default leannestage11event6 = 1
default leannestage11event7 = 1
default leannestage11event8 = 1
default leannestage12event = 1
default leannestage12event2 = 1
default leannestage12event3 = 1
default leannestage13event = 1
default leannestage13event2 = 1
default leannestage13event3 = 1
default tristastage1event = 1
default tristastage2event = 1
default tristastage3event = 1
default tristastage3phone = 1
default tristastage4event = 1
default tristastage6event = 1
default tristastage7event = 1
default tristastage8event = 1
default tristastage8phone = 1
default tristastage10event = 1
default lunastage3event = 1
default lunastage4event = 1
default lunastage5event = 1
default lunastage6event = 1
default lunastage7event = 1
default lunastage8event = 1
default lunastage9event = 1
default lunastage10event = 1
default lunastage10event2 = 1
default lunastage11event = 1
default lunastage12event = 1
default katrineintroduction = 1
default katrinestage1event = 1
default katrinestage2event = 1
default katrinestage3event = 1
default katrinestage4event = 1
default katrinestage5event = 1
default katrinestage5phone = 1
default katrinestage6event = 1
default katrinestage6phone = 1
default katrinestage7event = 1
default katrinestage8event = 1
default katrinestage9event = 1
default katrinestage10event = 1
default bonnieintroduction = 1
default bonniestage1event = 1
default bonniestage2event = 1
default bonniestage2event2 = 1
default bonniestage3event = 1
default bonniestage4event = 1
default bonniestage5event = 1
default bonniestage6event = 1
default bonniestage7event = 1
default bonniestage7event2 = 1
default bonniestage8event = 1
default bonniestage9event = 1
default bonniestage10event = 1
default bonniestage10phone = 1
default bonniestage11event = 1
default rebeccastage2event = 1
default rebeccastage3event = 1
default rebeccastage3phone = 1
default cayennestage1event = 1
default cayennestage1event2 = 1
default cayennestage1event3 = 1
default cayennestage1event4 = 1
default cayennestage1event5 = 1
default cayennestage2event = 1
default cayennestage3event = 1
default cayennestage4event = 1
default cayennestage5event = 1
default cayennestage6event = 1
default cayennestage7event = 1
default cayennestage8event = 1
default cayennestage9event = 1
default cayennestage10event = 1
default cayennestage11event = 1
default cayenneleave = 0
default nataliestage3event = 1
default nataliestage4event = 1
default nataliestage4event2 = 1
default sallystage3event = 1
default sallystage4event = 1
default brittastage4event = 1
default roxiestage4event = 1
default amberstage0event = 1
default amberstage1event = 1
default amberstage1event2 = 1
default amberstage2event = 1
default amberstage2event2 = 1
default amberstage3event = 1
default amberstage4event = 1
default amberstage5event = 1
default amberstage5event2 = 1
default amberstage6event = 1
default amberstage7event = 1
default lisastage0event = 1
default lisastage1event = 1
default lisastage1event2 = 1
default lisastage2event = 1
default lisastage2event2 = 1
default lisastage3event = 1
default lisastage3event2 = 1
default lisastage4event = 1
default lisastage4event2 = 1
default lisastage4phone = 1
default lisastage5event = 1
default lisastage6event = 1
default lisastage7event = 1
default lisastage7event2 = 1
default mayastage1event = 1
default mayastage1event2 = 1
default mayastage1event3 = 1
default mayastage2event = 1
default mayastage2event2 = 1
default mayastage2event3 = 1
default mayastage2event4 = 1
default mayastage3event = 1
default mayastage3event2 = 1
default mayastage3event3 = 1
default mayastage4event = 1
default mayastage4event2 = 1
default mayastage4event3 = 1
default mayastage4event4 = 1
default mayastage5event = 1
default mayastage5event2 = 1
default mayastage5event3 = 1
default mayastage5event4 = 1
default mayastage5event5 = 1
default mayastage6event = 1
default mariestage0event = 1
default mariestage1event = 1
default mariestage1event2 = 1
default mariestage2event = 1
default mariestage2event2 = 1
default mariestage3event = 1
default mariestage3event2 = 1
default mariestage4event = 1
default mariestage4event2 = 1
default mariestage5event = 1
default mariestage6event = 1
default mariestage6event2 = 1
default mariestage6event3 = 1
default mariestage7phone = 1
default haristage0event = 1
default haristage1event = 1
default haristage1event2 = 1
default haristage1event3 = 1
default haristage1event4 = 1
default haristage1event5 = 1
default haristage2event = 1
default haristage2event2 = 1
default haristage3event = 1
default haristage3event2 = 1
default haristage4event = 1
default haristage4event2 = 1
default haristage4event3 = 1
default haristage5event = 1
default haristage6event = 1
default haristage6event2 = 1
default haristage7event = 1
default hari_mad = 0
default bunnybitesgirlsstage2 = 1
default bunnybitesgirlsstage3 = 1
default mariestage3eventtrigger = 0
default daisycayennetutorintro = 1
default lunabunnybitesevent = 1
default carolineBBfirsttime = 1
default rebeccagymfirsttime = 1
default bonniegymfirsttime = 1
default lisagymfirsttime = 1
default mayagymfirsttime = 1
default amberprizefirsttime = 1
default bonnieprizefirsttime = 1
default katrineprizefirsttime = 1
default lisaprizefirsttime = 1
default marieprizefirsttime = 1
default tristaprizefirsttime = 1
default cayennebellyrubfirsttime = 1

#character stats unlocks
default luna_stats_visible = 0
default teacher_stats_visible = 0
default leanne_stats_visible = 0
default katrine_stats_visible = 0
default marie_stats_visible = 0
default lisa_stats_visible = 0
default amber_stats_visible = 0
default cayenne_stats_visible = 0
default maya_stats_visible = 0
default caroline_stats_visible = 0
default vicky_stats_visible = 0
default bonnie_stats_visible = 0
default rebecca_stats_visible = 0
default trista_stats_visible = 0
default britta_stats_visible = 0
default charlene_stats_visible = 0
default natalie_stats_visible = 0
default roxie_stats_visible = 0
default sally_stats_visible = 0
default mylenna_stats_visible = 0
default hari_stats_visible = 0
default amberundressoption = 0
default lisaundressoption = 0
default mayaundressoption = 0

#Character Story unlocks
default teacherstory = 0
default lunastory = 0
default leannestory = 0
default katrinestory = 0
default mariestory = 0
default lisastory = 0
default amberstory = 0
default cayennestory = 0
default mayastory = 0
default carolinestory = 0
default vickystory = 0
default bonniestory = 0
default rebeccastory = 0
default tristastory = 0
default brittastory = 0
default charlenestory = 0
default nataliestory = 0
default roxiestory = 0
default sallystory = 0
default mylennastory = 0
default haristory = 0

#location/activity unlocks
default streamergirlunlock = 0
default workunlock = 0
default libraryunlock = 0
default phoneunlock = 0
default gymunlock = 0
default animestoreunlock = 0

#Values that makes the bonnie logic work
default bonnie_ask_bigger = 0 #To make sure Bonnie doesn't keep asking if she is getting too big.
default bonnietits = 2 #To make sure that Bonnie shows her tits every second repeatable visit at her home.

#Value that switches between maya's dances
default mayadance = 0

#book unlocks
default kamasutravol1 = 0
default bellyrubs = 0
default workoutchampion = 0
default charismamastervol1 = 0
default charismamastervol2 = 0
default secretfeedervol1 = 0
default secretfeedervol2 = 0
default hagglelikeapro = 0
default sweettoothvol1 = 0
default sweettoothvol2 = 0

#book holding
default booksheld = 0
default kamasutravol1hold = 0
default bellyrubshold = 0
default workoutchampionhold = 0
default charismamastervol1hold = 0
default charismamastervol2hold = 0
default secretfeedervol1hold = 0
default secretfeedervol2hold = 0
default hagglelikeaprohold = 0
default sweettoothvol1hold = 0
default sweettoothvol2hold = 0

#book times read
default kamasutravol1times = 0
default bellyrubstimes = 0
default workoutchampiontimes = 0
default charismamastervol1times = 0
default charismamastervol2times = 0
default secretfeedervol1times = 0
default secretfeedervol2times = 0
default hagglelikeaprotimes = 0
default sweettoothvol1times = 0
default sweettoothvol2times = 0

#food unlocks
default corndogunlock = 0
default milkshakeunlock = 0
default onionringunlock = 0
default burritounlock = 0
default bbqunlock = 0

#teaching checks so it doesnt teach the same thing multiple times
default teaching_corndog_check = 0
default teaching_calories_times = 0
default teaching_calories_check = 0
default teaching_terminology_times = 0
default teaching_terminology_check = 0
default teaching_milkshake_check = 0
default teaching_onionring_check = 0
default teaching_bbq_check = 0
default teaching_hedonism_times = 0
default teaching_hedonism_check = 0
default teaching_addiction_times = 0
default teaching_addiction_check = 0
default teaching_industry_times = 0
default teaching_industry_check = 0
default teaching_animal_times = 0
default teaching_animal_check = 0
default teaching_bodytypes_times = 0
default teaching_bodytypes_check = 0
default teaching_naturenurture_times = 0
default teaching_naturenurture_check = 0
default teaching_indulgence_times = 0
default teaching_indulgence_check = 0
default teaching_careers_times = 0
default teaching_careers_check = 0
default teaching_feederfeedee_times = 0
default teaching_feederfeedee_check = 0
default teaching_fatphobia_times = 0
default teaching_fatphobia_check = 0
default teaching_socialfood_times = 0
default teaching_socialfood_check = 0
default teaching_clothing_times = 0
default teaching_clothing_check = 0
default teaching_gainingtips_times = 0
default teaching_gainingtips_check = 0
default teaching_leanneguest = 0
default teaching_gabeguest = 0
default teaching_bmi_check = 0
default teaching_bodyfat_check = 0

#One time questions for Leanne that happen during a date in Bunny Bites or Sugar Shop
default leannequestion1 = 1
default leannequestion2 = 1
default leannequestion3 = 1
default leannequestion4 = 1
default leannequestion5 = 1
default leannequestion6 = 1

default persistent.imperial = False
default persistent.masturbation = False
default persistent.needles = False
default persistent.nosexscene = False

#creates gestures for mobile
define config.gestures = { "n" : "game_menu", "s" : "hide_windows" }

label splashscreen:
    $renpy.movie_cutscene("images/bladerune.webm")
    scene savewarning
    pause
    scene disclaimer
    pause

    return

#starts here
label start:
    stop music fadeout 1.0

    if introcheck == 1:
        "Welcome to Fattening Career, this game is in early alpha development, which means there will be bugs and inconsistencies in images and story."
        "Any criticism and/or suggestions are appreciated on the Discord, Steam forums and Weightgaming forums."
        "This game contains sexual and fetish scenes, please confirm you are 18+."
        menu:
            "I am over 18":
                "I hope you will enjoy the game!"

            "I am not over 18":
                $ renpy.quit()
        "Sex scenes are enabled by default, you can toggle these off in the preferences menu."
        "The measurements are set to Metric by default, you can toggle them to the Imperial system in the preferences menu."
        "You are a twenty-one year old man returning home for the first time in three years."
        "After graduating you left to travel and see the sights, young and eager to get out of the small town you grew up in."
        "Now, three years later, you return home with a newfound sense of accomplishment."
        "You’ve set your sights on majoring in nutritional studies at the local university. Your parents inform you there has been an “economic boom” of sorts, as they have taken to calling it."
        "New places and unfamiliar sights have sprung up within the three years you’ve been gone from the once sleepy little hollow you used to call home."

        python:
            playername = renpy.input("What is the main character called? (Leave blank for default name.)")
            playername = playername.strip() or "David"
        #shows the current day on the top left corner
        $ introcheck = 0
        show screen Day
    call weight_check from _call_weight_check

    ## Mobile Phone
    $ unfreeze()

    $ messages = [] # list of all messages in the dialogue

    $ message_time = False # if True - get current time / or [hours, minutes] / or False
    $ in_history = True # add messages to history
    $ choice_number = True # default 1. choice1 / 2. choice2 / etc. / or False
    $ click_to_continue = False # if False - live mode messages
    $ time_to_send_pm = 2.0 # time to send picture message
    $ time_to_send_am = 2.0 # time to send audio message
    $ under_messenger = True # set False if you don't need a darker background under messenger

    $ typewriter = False # if False - you instantly send a message
    $ typewriter_speed = 2 # how fast you type

    $ interlocutor_name = "Luna" # interlocutor's name
    $ interlocutor_name_color = '#c4c4c4' # interlocutor's name color
    $ interlocutor_online = True # interlocutor status
    $ interlocutor_typing = False # if False - interlocutor instantly sends a message
    $ interlocutor_extra_time = 2.0 # extra writing time
    $ interlocutor_typing_speed = 0.05 # default speed 0.1 * number of letters

    $ groupchat_enable = False
    $ groupchat = GroupChat(name='Chat') # Group Chat Name
    $ groupchat.add( Interlocutor(ID=1, name='Luna', color='#fff68f') ) # Interlocutor 1
    $ groupchat.add( Interlocutor(ID=2, name='Katrine', color='#b73b87') ) # Interlocutor 2
    $ groupchat.add( Interlocutor(ID=3, name='Daisy', color='#009999') ) # Interlocutor 3
    $ groupchat.add( Interlocutor(ID=4, name='Leanne', color='#d6ff60') ) # Interlocutor 4
    $ active_groupchat = groupchat # Set Active Group Chat

    $ name = '[playername]' #Default name ###renpy.input(u"Who Am I?", length=25).title() # your name

    #selecting what kind of day it will be
    $ strip = 0
    if week == 1 and day == 1:
        scene university_outside
        pc "First day at the university. Hopefully this class won’t be too boring."
        jump Boring_Teacher

    elif week == 1 and day == 2:
        scene university_outside
        pc "Another day at the university, let's see what the teacher has in store for us today."
        jump Sexy_Teacher_Tuesday

    elif week == 1 and day == 3:
        scene university_outside
        pc "Another day at the university, let's see what the teacher has in store for us today."
        jump Sexy_Teacher_Wednesday

    elif week == 1 and day == 4:
        image amber_workattire_counter = "/amber/[amber.stage]/workattire_counter.webp"
        scene amber_workattire_counter
        play music "/music/bunny_bites.ogg" if_changed
        "Before going to class you pickup your order of fresh chicken nuggets."
        amber "Hey, good to see you, welcome back."
        amber "Here's your order."
        pc "Thank you!"
        scene university_outside
        stop music fadeout 1.0
        pc "Another day at the university. I hope Daisy likes the nuggets."
        jump Sexy_Teacher_Thursday

    elif week == 1 and day == 5:
        scene university_outside
        "The next morning you head to class with your bundle of sweets, eager to hand over the bounty to Daisy."
        pc "I got loads of food for the teacher."
        jump First_Friday

    elif day == 1 and teacherstage9event == 0 and carolinestage1event == 1:
        jump Caroline_Stage_1_Event

    elif week > 1 and day == 1:
        scene university_outside
        pc "It's Monday. Can't wait to see how much bigger Daisy got!"
        jump Monday

    elif day == 6:
        scene player_room
        pc "It's Saturday."
        jump Saturday

    elif day == 7:
        scene player_room
        pc "It's Sunday."
        jump Sunday

    elif day >= 8:
        $ day = 1
        $ week += 1
        jump start

    elif day >= 2 and teacherstage2event == 1 and teacher.stage >= 2:
        jump Teacher_Stage_2_Event

    elif day >= 2 and teacherstage3event == 1 and teacher.stage >= 3:
        jump Teacher_Stage_3_Event

    elif day == 2 and groupprojectstart == 0 and haristage1event == 1:
        jump Hari_Stage_1_Event_1

    elif day == 3 and haristage1event == 0 and haristage1event2 == 1:
        jump Hari_Stage_1_Event_2

    elif day == 4 and haristage1event2 == 0 and haristage1event3 == 1:
        jump Hari_Stage_1_Event_3

    elif day == 5 and haristage1event3 == 0 and haristage1event4 == 1:
        jump Hari_Stage_1_Event_4

    elif day == 2 and carolinestage1event == 0 and carolinestage1event2 == 1:
        jump Caroline_Stage_1_Event_2
                
    elif day == 3 and carolinestage1event2 == 0 and carolinestage1event3 == 1:
        jump Caroline_Stage_1_Event_3
                
    elif day == 4 and carolinestage1event3 == 0 and carolinestage1event4 == 1:
        jump Caroline_Stage_1_Event_4

    elif day == 5 and carolinestage1event5 == 1 and carolinestage1event4 == 0:
        jump Caroline_Stage_1_Event_5

    elif day == 2 and carolinestage2event == 1 and carolinestage1event5 == 0 and daycount4 >= 14:
        jump Caroline_Stage_2_Event

    elif day == 2 and vickystage1event == 1 and carolinestage1event5 == 0 and daycount4 >= 6:
        jump Vicky_Stage_1_Event
    
    elif day == 3 and vickystage1event2 == 1 and vickystage1event == 0:
        jump Vicky_Stage_1_Event_2

    elif day == 4 and vickystage1event3 == 1 and vickystage1event2 == 0:
        jump Vicky_Stage_1_Event_3

    elif day == 5 and vickystage1event4 == 1 and vickystage1event3 == 0:
        jump Vicky_Stage_1_Event_4

    elif day >= 2 and teacherstage4event == 1 and teacher.stage >= 4:
        jump Teacher_Stage_4_Event

    elif day >= 2 and teacherstage5event == 1 and teacher.stage >= 5:
        jump Teacher_Stage_5_Event

    elif day >= 2 and teacherstage6event == 1 and teacher.stage >= 6:
        jump Teacher_Stage_6_Event_1

    elif day >= 2 and teacherstage7event == 1 and teacher.stage >= 7:
        jump Teacher_Stage_7_Event

    elif day >= 2 and teacherstage8event == 1 and teacher.stage >= 8:
        jump Teacher_Stage_8_Event

    elif day >= 2 and teacherstage9event == 1 and teacher.stage >= 9:
        jump Teacher_Stage_9_Event_1

    elif day >= 2 and teacherstage10event == 1 and teacher.stage >= 10:
        jump Teacher_Stage_10_Event

    elif day >= 2 and teacherstage11event == 1 and teacher.stage >= 11:
        jump Teacher_Stage_11_Event

    #elif day >= 2 and teacherstage13event == 1 and teacher.stage >= 13:
    #    jump Teacher_Stage_13_Event

    elif day >= 2 and teacherstage14event == 1 and teacher.stage >= 14 and luna.stage >= 10:
        jump Teacher_Stage_14_Event

    elif day >= 2 and teacherstage14event == 1 and teacher.stage >= 14 and luna.stage == 8:
        jump Teacher_Stage_14_Event

    elif week > 1 and day == 5:
        scene university_outside
        pc "It's Friday! Daisy told us we can give her stuff for her to eat over the weekend."
        jump Friday

    else:
        $ rng = renpy.random.randint(1,100)
        if rng >= 90:
            scene player_room
            "You wake up to the sound of a heavy storm."
            scene outside_rainy
            "Knowing the weather will heavily impact your normally dry commute, you quickly get ready and hastily head out into the storm."
            scene university_outside_rain
            "Trudging through puddles, you manage to make it to class with minutes to spare."
            scene university_sitdown
            "Taking your seat, you look around the room to see everyone in various states of being drenched. This also rings true for Daisy as she arrives to class."
            image uni_sexy_teacher_wet1 = "/teacher/[teacher.stage]/0/wet1.webp"
            scene uni_sexy_teacher_wet1
            "Rushing into the room, Daisy leans on the side of her desk as she catches her breath."
            "The constant rise and fall of her chest allows the entire class to see the way her soaked clothing shows practically everything beneath the fabric."
            teacher "Sorry I’m late. This storm came out of nowhere. Give me a moment to dry off a bit before we begin."
            image uni_sexy_teacher_wet2 = "/teacher/[teacher.stage]/0/wet2.webp"
            scene uni_sexy_teacher_wet2
            "Showing very little hesitation, Daisy drops her dripping skirt to the ground and kicks it to the side."
            "Unclasping the buttons on her shirt, she opens up her top to leave most of her torso fully visible."
            image uni_sexy_teacher_wet3 = "/teacher/[teacher.stage]/0/wet3.webp"
            scene uni_sexy_teacher_wet3
            "Still not satisfied, she continues to discard one piece of clothing after another."
            "Left wearing only her glasses, panties, and pasties on her nipples, she hangs up her clothing and returns to the front of the class."
            teacher "There, much better. Now as for today’s lesson…"
            "The rest of the class is a blur to you. Though you can hear her just fine, you can’t help but stare at her dripping wet body the entire length of her lecture."
            "The few times you’re able to look away from her, you see that the other students are equally mesmerized by the bizarre sight."
            "Giving up on learning anything useful for the day, you spend the rest of the class gawking at her figure until the lecture is over."
            if haristage1event4 == 0:
                menu:
                    "Study with Hari." if hari_mad == 0:
                        #EVENTS
                        if haristage1event4 == 0 and haristage1event5 == 1 and hari_study_times == 0:
                            jump Hari_Stage_1_Event_5
                        elif haristage1event5 == 0 and haristage2event == 1 and hari_study_times == 0 and hari.stage >= 2:
                            jump Hari_Stage_2_Event_1
                        elif haristage2event2 == 0 and haristage3event == 1 and hari_study_times == 0 and hari.stage >= 3:
                            jump Hari_Stage_3_Event_1
                        elif haristage3event == 0 and haristage3event2 == 1 and hari_study_times == 0 and hari.weight >= 64:
                            jump Hari_Stage_3_Event_2
                        elif haristage4event == 0 and haristage4event2 == 1 and hari_study_times == 0 and hari.stage >= 4:
                            jump Hari_Stage_4_Event_2
                        elif haristage5event == 0 and haristage6event == 1 and hari_study_times == 0 and hari.stage >= 6:
                            jump Hari_Stage_6_Event_1

                        #REPEATABLES
                        if hari_study_times == 0:
                            call Hari_study_1
                        elif hari_study_times == 1:
                            call Hari_study_2
                        elif hari_study_times == 2:
                            call Hari_study_3
                        stop music fadeout 1.0
                        $ actions = 4
                        $ strip = 0
                        $ eatcount = 0
                        $ daytime = 2
                        jump freetime

                    "Study with Caroline." if carolinestage2event == 0:
                        #EVENTS
                        if carolinestage2event2 == 1 and carolinestage2event == 0 and caroline_study_times == 0:
                            jump Caroline_Stage_2_Event_2
                        if carolinestage2event4 == 1 and carolinestage2event3 == 0 and caroline_study_times == 0 and caroline.weight >= 81:
                            jump Caroline_Stage_2_Event_4

                        #REPEATABLES
                        if caroline_study_times == 0:
                            call Caroline_study_1
                        elif caroline_study_times == 1:
                            call Caroline_study_2
                        elif caroline_study_times == 2:
                            call Caroline_study_3
                        stop music fadeout 1.0
                        $ actions = 4
                        $ strip = 0
                        $ eatcount = 0
                        $ daytime = 2
                        jump freetime

                    "Study with Vicky." if vickystage1event4 == 0:
                        #EVENTS
                        if vickystage2event == 1 and vickystage1event4 == 0 and vicky_study_times == 0:
                            jump Vicky_Stage_2_Event

                        #REPEATABLES
                        if vicky_study_times == 0:
                            call Vicky_study_1
                        elif vicky_study_times == 1:
                            call Vicky_study_2
                        elif vicky_study_times == 2:
                            call Vicky_study_3
                        stop music fadeout 1.0
                        $ actions = 4
                        $ strip = 0
                        $ eatcount = 0
                        $ daytime = 2
                        jump freetime

                    "Go home.":
                        "You decide to head home."
                        stop music fadeout 1.0
                        $ actions = 4
                        $ strip = 0
                        $ eatcount = 0
                        $ daytime = 2
                        jump freetime
            stop music fadeout 1.0
            $ actions = 4
            $ strip = 0
            $ eatcount = 0
            $ daytime = 2
            jump freetime
        scene university_outside
        jump Normal_Day

label Saturday:
    $ daytime = 1
    jump freetime

label Sunday:
    $ daytime = 1
    jump freetime

label Monday:
    #Mondays are when the teacher does a weigh in
    if carolinestage1event4 == 0 and carolinestage2event == 1:
        scene university_looking_into_class3
    else:
        scene university_looking_into_class
    play music "/music/university.ogg" if_changed
    "You mentally prepare yourself for another crazy week in Daisy's class."
    image uni_sexy_teacher_arrive = "/teacher/[teacher.stage]/0/arrive.webp"
    scene uni_sexy_teacher_arrive
    window hide
    pause
    image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
    scene uni_sexy_teacher_greet
    teacher "Good morning, students."
    s "Good morning, Ms. Tanwen."
    call rngteachingscene from _call_rngteachingscene_67
    teacher "I hope you all had a great weekend."
    $ rnggym = renpy.random.randint(1,100)
    if rnggym >= 50 and leanne.stage >= 13 and teaching_leanneguest == 0:
        if leannechoice == 1:
            call lyn_guest_lecture
            $ strip = 0
            $ daytime = 2
            jump freetime
        elif leannechoice == 2:
            call leanne_guest_lecture
            $ strip = 0
            $ daytime = 2
            jump freetime
    $ strip += 1
    teacher "I certainly did with all of the food and drinks you gave me."
    $ strip += 1
    teacher "Before we do our weekly measure, let's get these clothes out of the way."
    $ strip += 1
    window hide
    pause
    $ strip += 1
    pause
    teacher "Now that that’s out of the way, please get out your notes. It’s time to measure."
    image uni_sexy_teacher_measure_belly1 = "/teacher/[teacher.stage]/4/measure_belly1.webp"
    scene uni_sexy_teacher_measure_belly1
    if persistent.imperial:
        $ imperialweight = (teacher.weight * 2.2)
        teacher "Let’s see. Right now I weigh [imperialweight:.02f] lbs."
    else:
        teacher "Let’s see. Right now I weigh [teacher.weight:.02f] kg."
    image uni_sexy_teacher_measure_belly2 = "/teacher/[teacher.stage]/4/measure_belly2.webp"
    scene uni_sexy_teacher_measure_belly2
    if persistent.imperial:
        teacher "And my waistline is [teacher.waist_size:.02f] inches."
    else:
        $ metricwaist_size = (teacher.waist_size * 2.54)
        teacher "And my waistline is [metricwaist_size:.02f] cm."
    image uni_sexy_teacher_measure_ass1 = "/teacher/[teacher.stage]/4/measure_ass1.webp"
    scene uni_sexy_teacher_measure_ass1
    if persistent.imperial:
        teacher "My hips are about [teacher.ass_size:.02f] inches wide."
    else:
        $ metricass_size = (teacher.ass_size * 2.54)
        teacher "My hips are about [metricass_size:.02f] cm wide."
    image uni_sexy_teacher_measure_breasts1 = "/teacher/[teacher.stage]/3/measure_breasts1.webp"
    scene uni_sexy_teacher_measure_breasts1
    if persistent.imperial:
        $ imperialbreastweight = (teacher.breast_weight * 2.2)
        teacher "My breasts measure [imperialbreastweight:.02f]lbs."
    else:
        teacher "My breasts measure [teacher.breast_weight:.02f]kg."
    image uni_sexy_teacher_measure_breasts2 = "/teacher/[teacher.stage]/3/measure_breasts2.webp"
    scene uni_sexy_teacher_measure_breasts2
    if persistent.imperial:
        teacher "My bosom is currently a [teacher.breast_cup] cup, with a bust circumference of [teacher.breast_size:.02f] inches."
    else:
        $ metricbreast_size = (teacher.breast_size * 2.54)
        teacher "My bosom is currently a [teacher.breast_cup] cup, with a bust circumference of [metricbreast_size:.02f] cm."
    call rngshowoffscene from _call_rngshowoffscene_4
    teacher "I hope you all wrote that down. It is very important to record my progress."

    if haristage0event == 0 and groupprojectstart == 1 and carolineintro3 == 0:
        call Group_Project_start from _call_Group_Project_start
        jump freetime
    call dialogue_choices from _call_dialogue_choices_1
    call rngshowoffscene from _call_rngshowoffscene_5
    teacher "That's it for today. See you all tomorrow!"
    if haristage0event == 1 and teacherstage3event == 0 and teacher.stage >= 3:
        call Hari_Stage_0_Event from _call_Hari_Stage_0_Event
    if teacher.weight >= 70 and daisycayennetutorintro == 1 and cayennestage1event5 == 0:
        call Daisy_Cayenne_tutor_intro from _call_Daisy_Cayenne_tutor_intro
    stop music fadeout 1.0
    if katrinestage8event == 1 and katrine.stage >= 8 and tristastage7event == 0:
        call Katrine_Stage_8_Event from _call_Katrine_Stage_8_Event
        $ strip = 0
        $ daytime = 3

        jump freetime
    scene university_leave
    "You head home for the day."
    $ strip = 0
    $ daytime = 2

    jump freetime

label Friday:
    #(NOTE: The following should play out during a regular, Friday class. In the event that the player has done enough study sessions with one of the students, that will play out instead.)
    #IMAGE: Outside of the classroom
    if carolinestage1event4 == 0 and carolinestage2event == 1:
        scene university_looking_into_class3
    else:
        scene university_looking_into_class
    play music "/music/university.ogg" if_changed
    "You arrive to class."
    "Today is Daisy's feeding day. What will you bring?"
    #(NOTE: The choices will determine how many feeding scenes the player gets to watch for the class. A=1, B=2, and C=3. Options B and C will only be available if the player bought the necessary supplies beforehand.)
    menu:
        "Nothing.":
            image uni_sexy_teacher_arrive = "/teacher/[teacher.stage]/0/arrive.webp"
            scene uni_sexy_teacher_arrive
            window hide
            pause
            image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
            scene uni_sexy_teacher_greet
            teacher "Good morning students."
            s "Good morning Ms. Tanwen."
            if hari_study_times == 3:
                call Hari_study_4 from _call_Hari_study_4
            elif caroline_study_times == 3:
                call Caroline_study_4
            elif vicky_study_times == 3:
                call Vicky_study_4
            call rngteachingscene from _call_rngteachingscene_68
            teacher "Today is feeding day, so give me a moment to get ready."
            $ strip += 1
            window hide
            pause
            $ strip += 1
            pause
            $ strip += 1
            pause
            $ strip += 1
            pause
            image uni_sexy_teacher_food_teaching1 = "/teacher/[teacher.stage]/[strip]/food_teaching1.webp"
            scene uni_sexy_teacher_food_teaching1
            teacher "So many great options. Let’s see what I should start with."
            call foodchoice from _call_foodchoice
            image uni_sexy_teacher_stuffed_half = "/teacher/[teacher.stage]/[strip]/stuffed_half.webp"
            scene uni_sexy_teacher_stuffed_half
            teacher "Delicious as always. I’ll finish up the rest of this over the weekend. See you all again on Monday!"
            stop music fadeout 1.0
            scene university_leave
            "You head home to enjoy the weekend."
            $ eatcount = 0
            $ strip = 0
            $ daytime = 2
            jump freetime
        "A small offering. (-1 meals)" if foodheld >= 1:
            $ foodheld -= 1
            image uni_sexy_teacher_arrive = "/teacher/[teacher.stage]/0/arrive.webp"
            scene uni_sexy_teacher_arrive
            window hide
            pause
            image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
            scene uni_sexy_teacher_greet
            teacher "Good morning students."
            s "Good morning Ms. Tanwen."
            if hari_study_times == 3:
                call Hari_study_4 from _call_Hari_study_4_1
            elif caroline_study_times == 3:
                call Caroline_study_4
            elif vicky_study_times == 3:
                call Vicky_study_4
            call rngteachingscene from _call_rngteachingscene_275
            teacher "Today is feeding day, so give me a moment to get ready."
            $ strip += 1
            window hide
            pause
            $ strip += 1
            pause
            $ strip += 1
            pause
            $ strip += 1
            pause
            image uni_sexy_teacher_food_teaching2 = "/teacher/[teacher.stage]/[strip]/food_teaching2.webp"
            scene uni_sexy_teacher_food_teaching2
            teacher "So many great options. Let’s see what I should start with."
            call foodchoice from _call_foodchoice_1
            teacher "Mmm, that was pretty good. What’s next?"
            call foodchoice from _call_foodchoice_2
            image uni_sexy_teacher_stuffed = "/teacher/[teacher.stage]/[strip]/stuffed.webp"
            scene uni_sexy_teacher_stuffed
            teacher "Delicious as always. I’ll finish up the rest of this over the weekend. See you all again on Monday!"
            stop music fadeout 1.0
            scene university_leave
            "You head home to enjoy the weekend."
            $ eatcount = 0
            $ strip = 0
            $ daytime = 2
            jump freetime
        "A large offering. (-3 meals)" if foodheld >= 3:
            $ foodheld -= 3
            image uni_sexy_teacher_arrive = "/teacher/[teacher.stage]/0/arrive.webp"
            scene uni_sexy_teacher_arrive
            window hide
            pause
            image uni_sexy_teacher_greet = "/teacher/[teacher.stage]/0/greet.webp"
            scene uni_sexy_teacher_greet
            teacher "Good morning students."
            s "Good morning Ms. Tanwen."
            if hari_study_times == 3:
                call Hari_study_4 from _call_Hari_study_4_2
            elif caroline_study_times == 3:
                call Caroline_study_4
            elif vicky_study_times == 3:
                call Vicky_study_4
            call rngteachingscene from _call_rngteachingscene_276
            teacher "Today is feeding day, so give me a moment to get ready."
            $ strip += 1
            window hide
            pause
            $ strip += 1
            pause
            $ strip += 1
            pause
            $ strip += 1
            pause
            image uni_sexy_teacher_food_teaching3 = "/teacher/[teacher.stage]/[strip]/food_teaching3.webp"
            scene uni_sexy_teacher_food_teaching3
            teacher "So many great options. Let’s see what I should start with."
            call foodchoice from _call_foodchoice_7
            teacher "Mmm, that was pretty good. What’s next?"
            call foodchoice from _call_foodchoice_8
            teacher "I’m feeling pretty stuffed, but I think I can do one more."
            call foodchoice from _call_foodchoice_9
            image uni_sexy_teacher_stuffed_full = "/teacher/[teacher.stage]/[strip]/stuffed_full.webp"
            scene uni_sexy_teacher_stuffed_full
            teacher "Delicious as always. I’ll finish up the rest of this over the weekend. See you all again on Monday!"
            stop music fadeout 1.0
            scene university_leave
            "You head home to enjoy the weekend."
            $ eatcount = 0
            $ strip = 0
            $ daytime = 2
            jump freetime

label Normal_Day:
    if carolinestage1event4 == 0 and carolinestage2event == 1:
        scene university_looking_into_class3
    else:
        scene university_looking_into_class
    play music "/music/university.ogg" if_changed
    if haristage1event4 == 0:
        if vickyintro3 == 1 and vickyintro2 == 0 and day == 4 and teacher.stage >= 5:
            call Vicky_Intro3 from _call_Vicky_Intro3
            "You're given the option of how you would like to spend your class time."
        else:
            "Arriving at the university, you're given the option of how you would like to spend your class time."
        menu:
            "Go to class.":
                call Daisy_Class_Normal from _call_Daisy_Class_Normal
                $ actions = 4
                $ strip = 0
                $ eatcount = 0
                $ daytime = 2
                stop music fadeout 1.0
                "You head home for the day."
                jump freetime
            "Study with Hari." if hari_mad == 0:
                #EVENTS
                if haristage1event4 == 0 and haristage1event5 == 1 and hari_study_times == 0:
                    jump Hari_Stage_1_Event_5
                elif haristage1event5 == 0 and haristage2event == 1 and hari_study_times == 0 and hari.stage >= 2:
                    jump Hari_Stage_2_Event_1
                elif haristage2event2 == 0 and haristage3event == 1 and hari_study_times == 0 and hari.stage >= 3:
                    jump Hari_Stage_3_Event_1
                elif haristage3event == 0 and haristage3event2 == 1 and hari_study_times == 0 and hari.weight >= 64:
                    jump Hari_Stage_3_Event_2
                elif haristage4event == 0 and haristage4event2 == 1 and hari_study_times == 0 and hari.stage >= 4:
                    jump Hari_Stage_4_Event_2
                elif haristage5event == 0 and haristage6event == 1 and hari_study_times == 0 and hari.stage >= 6:
                    jump Hari_Stage_6_Event_1

                #REPEATABLES
                if hari_study_times == 0:
                    call Hari_study_1 from _call_Hari_study_1
                elif hari_study_times == 1:
                    call Hari_study_2 from _call_Hari_study_2
                elif hari_study_times == 2:
                    call Hari_study_3 from _call_Hari_study_3
                stop music fadeout 1.0
                $ actions = 4
                $ strip = 0
                $ eatcount = 0
                $ daytime = 2
                jump freetime
            #"Study with Vicky.":

            "Study with Caroline." if carolinestage2event == 0:
                #EVENTS
                if carolinestage2event2 == 1 and carolinestage2event == 0 and caroline_study_times == 0:
                    jump Caroline_Stage_2_Event_2
                if carolinestage2event4 == 1 and carolinestage2event3 == 0 and caroline_study_times == 0 and caroline.weight >= 81:
                    jump Caroline_Stage_2_Event_4

                #REPEATABLES
                if caroline_study_times == 0:
                    call Caroline_study_1
                elif caroline_study_times == 1:
                    call Caroline_study_2
                elif caroline_study_times == 2:
                    call Caroline_study_3
                stop music fadeout 1.0
                $ actions = 4
                $ strip = 0
                $ eatcount = 0
                $ daytime = 2
                jump freetime

            "Study with Vicky." if vickystage1event4 == 0:
                #EVENTS
                if vickystage2event == 1 and vickystage1event4 == 0 and vicky_study_times == 0:
                    jump Vicky_Stage_2_Event

                #REPEATABLES
                if vicky_study_times == 0:
                    call Vicky_study_1
                elif vicky_study_times == 1:
                    call Vicky_study_2
                elif vicky_study_times == 2:
                    call Vicky_study_3
                stop music fadeout 1.0
                $ actions = 4
                $ strip = 0
                $ eatcount = 0
                $ daytime = 2
                jump freetime



    else:
        if carolineintro2 == 1 and carolineintro1 == 0 and day == 4:
            call Caroline_Intro2 from _call_Caroline_Intro2
        elif carolineintro3 == 1 and carolineintro2 == 0 and day == 2:
            call Caroline_Intro3 from _call_Caroline_Intro3
        else:
            "Arriving at the university, you sit down in your usual spot."
        call Daisy_Class_Normal from _call_Daisy_Class_Normal_1
        $ actions = 4
        $ strip = 0
        $ eatcount = 0
        $ daytime = 2
        stop music fadeout 1.0
        "You head home for the day."
        jump freetime






    #Daily Loop with choices, feeding, stripping and weight gain
    call rngteachingscene from _call_rngteachingscene_69
    if actions > 0:
        play music "/music/university.ogg" if_changed
        teacher "Okay class, does anyone have a suggestion for an activity for me to demonstrate?"
        pc "What should I suggest?"

        menu:

            "Have Daisy eat or drink something." if eatcount <= 1 and strip == 4:
                call foodchoice from _call_foodchoice_3
                $ actions -= 1
                jump Normal_Day

            "Read a book." if strip == 0 and booksheld >= 1:
                $ bookday = 2
                call book_read from _call_book_read_1
                $ actions -= 4
                jump Normal_Day

            "Let Daisy strip!" if strip == 0:
                if strip < 4:
                    $ strip += 1
                    window hide
                    pause
                    $ strip += 1
                    pause
                    $ strip += 1
                    pause
                    $ strip += 1
                    pause
                    $ actions -= 1
                    jump Normal_Day
                else:
                    "already fully stripped"
                    jump Normal_Day

            "Ask Daisy to show off." if strip == 4:
                call rngshowoffscene from _call_rngshowoffscene_7
                window hide
                pause
                call rngshowoffscene from _call_rngshowoffscene_8
                pause
                $ actions -= 1
                jump Normal_Day

            "Ask Daisy to show her ass." if strip == 4:
                image uni_sexy_teacher_showoffass1 = "/teacher/[teacher.stage]/4/showoffass1.webp"
                scene uni_sexy_teacher_showoffass1
                window hide
                pause
                image uni_sexy_teacher_showoffass2 = "/teacher/[teacher.stage]/4/showoffass2.webp"
                scene uni_sexy_teacher_showoffass2
                pause
                image uni_sexy_teacher_showoffass3 = "/teacher/[teacher.stage]/4/showoffass3.webp"
                scene uni_sexy_teacher_showoffass3
                pause
                $ actions -= 1
                jump Normal_Day

            "Ask Daisy to show her tits." if strip == 4:
                image uni_sexy_teacher_showoffbreasts1 = "/teacher/[teacher.stage]/4/showoffbreasts1.webp"
                scene uni_sexy_teacher_showoffbreasts1
                window hide
                pause
                image uni_sexy_teacher_showoffbreasts2 = "/teacher/[teacher.stage]/4/showoffbreasts2.webp"
                scene uni_sexy_teacher_showoffbreasts2
                pause
                image uni_sexy_teacher_showoffbreasts3 = "/teacher/[teacher.stage]/4/showoffbreasts3.webp"
                scene uni_sexy_teacher_showoffbreasts3
                pause
                $ actions -= 1
                jump Normal_Day

            "Ask Daisy to show her belly." if strip == 4:
                image uni_sexy_teacher_showoffbelly1 = "/teacher/[teacher.stage]/4/showoffbelly1.webp"
                scene uni_sexy_teacher_showoffbelly1
                window hide
                pause
                image uni_sexy_teacher_showoffbelly2 = "/teacher/[teacher.stage]/4/showoffbelly2.webp"
                scene uni_sexy_teacher_showoffbelly2
                pause
                image uni_sexy_teacher_showoffbelly3 = "/teacher/[teacher.stage]/4/showoffbelly3.webp"
                scene uni_sexy_teacher_showoffbelly3
                pause
                $ actions -= 1
                jump Normal_Day

    else:
        teacher "That's it for today, see all of you tomorrow!"
        stop music fadeout 1.0
        scene university_leave
        "You leave class for the day and make your way home."
        $ actions = 4
        $ strip = 0
        $ eatcount = 0
        $ daytime = 2
        jump freetime
