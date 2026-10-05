init python:

    char_weight = {
        'amber' : [0, 50, 53, 57, 61, 66, 72, 78, 85, 93, 101, 110, 120, 145],
        'bonnie' : [0, 70, 73, 76, 79, 82, 86, 90, 96, 103, 111, 120, 130, 142],
        'britta' : [0, 68, 72, 78, 87],
        'caroline' : [0, 76, 79, 82, 86, 90],
        'cayenne' : [0, 50, 53, 56, 60, 65, 70, 73, 77, 82, 87, 93],
        'charlene' : [0, 78, 86, 98, 118],
        'hari' : [0, 47, 50, 55, 61, 69, 77, 84, 96],
        'katrine' : [0, 80, 84, 88, 92, 97, 102, 108, 114, 120, 126, 136],
        'leanne' : [0, 53, 55, 58, 62, 66, 70, 74, 78, 82, 87, 92, 116, 123, 132, 152],
        'lisa' : [0, 54, 57, 60, 64, 68, 73, 78, 83, 88, 94, 99, 110],
        'luna' : [0, 54, 58, 62, 66, 71, 76, 80, 85, 90, 95, 101, 108],
        'marie' : [0, 60, 65, 69, 74, 79, 85, 91, 97, 104, 112, 122],
        'maya' : [0, 77, 80, 84, 88, 93, 98, 103, 109, 116, 123, 130],
        'mylenna' : [0, 54, 63],
        'natalie' : [0, 64, 70, 79, 90],
        'rebecca' : [0, 82, 88, 93],
        'roxie' : [0, 61, 65, 72, 79],
        'sally' : [0, 74, 80, 90, 104],
        'daisy' : [0, 52, 55, 58, 61, 64, 68, 72, 77, 82, 86, 91, 95, 100, 106, 112, 120, 130],
        'trista' : [0, 78, 82, 86, 90, 94, 98, 102, 106, 110, 115, 124, 138, 158],
        'vicky' : [0, 92, 98, 108, 120, 132],
    }
    char_waist = {
        'amber' : [0, 25.2, 28.9, 29.6, 32.5, 35.4, 37.6, 39.1, 40.7, 42.4, 44.6, 46.9, 50.8, 58.1],
        'bonnie' : [0, 25.0, 25.7, 26.7, 27.4, 28.3, 29.6, 30.0, 33.6, 34.9, 38.3, 40.3, 43.4, 47.0],
        'britta' : [0, 27.0, 27.3, 28.0, 29.2],
        'caroline' : [0, 24.8, 25.8, 28.2, 29.6, 30.6],
        'cayenne' : [0, 24.8, 25.7, 26.6, 27.3, 27.9, 28.6, 29.4, 30.3, 31.6, 33.3, 35.4],
        'charlene' : [0, 26.2, 30.9, 36.1, 41.2],
        'hari' : [0, 22.6, 23.4, 25.0, 27.8, 30.4, 31.6, 34.0, 39.7],
        'katrine' : [0, 29.1, 30.3, 31.8, 33.4, 34.3, 36.3, 38.5, 40.6, 43.0, 45.8, 50.4],
        'leanne' : [0, 23.9, 24.8, 25.7, 27.0, 28.8, 29.5, 29.8, 30.4, 31.2, 32.2, 33.1, 44.6, 46.9, 49.1, 56.5],
        'lisa' : [0, 24.6, 26.1, 27.5, 29.6, 30.6, 31.7, 33.1, 34.5, 35.7, 38.2, 40.4, 42.7],
        'luna' : [0, 23.4, 25.8, 27.3, 28.6, 30.3, 31.2, 33.0, 34.3, 35.7, 36.9, 37.3, 38.6],
        'marie' : [0, 24.6, 29.8, 33.0, 35.2, 37.2, 38.8, 41.0, 42.3, 43.9, 45.3, 47.3],
        'maya' : [0, 24.7, 25.9, 27.0, 28.1, 29.5, 30.8, 31.7, 33.3, 35.2, 37.5, 39.9],
        'mylenna' : [0, 22.8, 23.3],
        'natalie' : [0, 23.9, 24.3, 25.8, 31.9],
        'rebecca' : [0, 26.9, 27.1, 29.2],
        'roxie' : [0, 22.2, 22.7, 24.3, 26.0],
        'sally' : [0, 25.7, 27.6, 31.0, 34.9],
        'daisy' : [0, 23.1, 24.6, 26.3, 28.0, 29.6, 31.1, 32.8, 34.0, 35.7, 37.0, 40.4, 41.7, 43.6, 45.3, 46.9, 50.0, 53.6],
        'trista' : [0, 24.6, 25.4, 26.3, 27.0, 27.8, 28.2, 29.0, 29.7, 30.6, 32.6, 37.6, 42.3, 48.4],
        'vicky' : [0, 26.9, 29.7, 32.1, 34.1, 36.0],
    }
    char_ass = {
        'amber' : [0, 35.2, 38.8, 38.9, 41.7, 41.7, 43.8, 45.1, 46.8, 47.4, 48.1, 49.5, 51.0, 55.3],
        'bonnie' : [0, 42.8, 43.8, 45.2, 46.2, 47.4, 48.7, 50.6, 53.1, 54.7, 57.0, 59.6, 62.2, 65.4],
        'britta' : [0, 41.5, 41.9, 43.1, 45.0],
        'caroline' : [0, 39.0, 40.1, 40.4, 40.6, 40.9],
        'cayenne' : [0, 35.2, 37.0, 38.6, 39.8, 41.0, 42.3, 43.8, 45.4, 46.7, 48.2, 50.1],
        'charlene' : [0, 38.8, 42.6, 47.4, 49.6],
        'hari' : [0, 41.3, 42.6, 43.9, 47.5, 49.3, 50.5, 53.8, 56.5],
        'katrine' : [0, 43.7, 45.8, 48.2, 49.6, 50.4, 52.2, 52.7, 54.0, 55.0, 57.2, 59.1],
        'leanne' : [0, 35.1, 36.3, 37.3, 38.9, 40.5, 41.5, 42.3, 43.1, 44.0, 45.0, 45.9, 57.3, 59.1, 59.3, 64.1],
        'lisa' : [0, 34.9, 36.4, 37.9, 39.7, 41.7, 43.9, 46.5, 48.1, 49.4, 51.8, 54.2, 58.3],
        'luna' : [0, 36.3, 38.3, 39.6, 40.8, 42.5, 43.1, 44.3, 45.3, 46.7, 48.0, 49.2, 50.4],
        'marie' : [0, 37.5, 40.4, 42.0, 43.9, 45.5, 47.1, 48.9, 50.1, 50.8, 52.0, 53.8],
        'maya' : [0, 40.3, 41.5, 42.5, 43.5, 44.7, 45.9, 46.3, 47.6, 48.9, 50.2, 52.4],
        'mylenna' : [0, 37.2, 38.1],
        'natalie' : [0, 41.5, 42.6, 45.3, 49.0],
        'rebecca' : [0, 46.3, 47.8, 49.3],
        'roxie' : [0, 37.1, 38.3, 41.0, 43.8],
        'sally' : [0, 39.7, 45.0, 50.1, 56.0],
        'daisy' : [0, 37.2, 38.6, 40.0, 41.0, 41.4, 42.3, 43.7, 44.0, 45.0, 45.6, 46.9, 47.3, 48.6, 50.0, 51.5, 53.0, 53.9],
        'trista' : [0, 42.7, 44.0, 45.4, 46.7, 47.8, 48.2, 50.4, 51.7, 53.1, 53.8, 54.9, 58.9, 63.9],
        'vicky' : [0, 43.6, 46.0, 49.1, 51.9, 55.9],
    }
    char_boobs = {
        'amber' : [0, 33.6, 34.9, 34.9, 35.2, 35.7, 36.2, 36.6, 38.0, 38.8, 39.4, 40.3, 42.9, 51.3],
        'bonnie' : [0, 36.2, 36.7, 37.7, 38.4, 39.1, 39.7, 40.3, 41.4, 42.8, 44.0, 45.4, 46.6, 47.9],
        'britta' : [0, 34.3, 38.5, 44.2, 46.9],
        'caroline' : [0, 35.3, 36.9, 39.1, 40.8, 41.9],
        'cayenne' : [0, 36.2, 37.0, 37.8, 38.6, 39.3, 40.0, 40.8, 42.4, 43.4, 44.5, 45.9],
        'charlene' : [0, 37.2, 39.3, 41.9, 46.2],
        'hari' : [0, 30.1, 30.6, 30.8, 31.7, 32.9, 33.4, 34.4, 36.9],
        'katrine' : [0, 40.1, 41.7, 42.0, 42.4, 42.7, 42.7, 42.8, 42.9, 42.9, 43.6, 46.4],
        'leanne' : [0, 34.2, 35.2, 36.0, 36.9, 37.8, 38.4, 39.1, 39.5, 40.0, 41.2, 42.7, 50.5, 51.2, 52.3, 58.4],
        'lisa' : [0, 38.0, 39.0, 40.4, 40.7, 42.6, 44.7, 46.9, 47.3, 47.8, 47.9, 48.0, 49.9],
        'luna' : [0, 36.3, 37.5, 38.9, 40.5, 43.1, 44.4, 45.8, 48.1, 50.3, 52.3, 54.5, 56.2],
        'marie' : [0, 32.2, 33.9, 34.8, 35.5, 37.0, 37.6, 38.6, 39.2, 40.2, 40.7, 41.2],
        'maya' : [0, 41.0, 42.3, 43.4, 44.4, 45.5, 46.6, 46.8, 48.0, 49.0, 50.2, 51.7],
        'mylenna' : [0, 34.8, 37.3],
        'natalie' : [0, 32.9, 38.2, 42.4, 50.4],
        'rebecca' : [0, 38.8, 40.8, 42.2],
        'roxie' : [0, 33.8, 36.4, 41.4, 46.3],
        'sally' : [0, 35.6, 39.0, 42.7, 48.1],
        'daisy' : [0, 36.2, 36.4, 36.5, 37.0, 37.1, 37.6, 38.2, 38.2, 38.7, 38.8, 39.4, 39.7, 39.8, 40.6, 41.4, 42.8, 45.8],
        'trista' : [0, 35.7, 36.0, 36.2, 36.5, 36.7, 36.9, 37.2, 37.4, 37.7, 38.9, 39.9, 44.7, 47.9],
        'vicky' : [0, 39.8, 41.2, 42.0, 44.4, 45.9],
    }
    char_cup = {
        'amber' : [0, "30C", "32C", "32C", "32C", "34B", "34B", "36A", "36B", "38A", "38A", "40AA", "44AA", "50AA"],
        'bonnie' : [0, "32D", "32E", "32E", "34E", "34E", "34E", "36E", "36E", "38E", "38E", "40E", "42E", "42F"],
        'britta' : [0, "32B", "34D", "36H", "38I"],
        'caroline' : [0, "32C", "34D", "34E", "34G", "34G"],
        'cayenne' : [0, "32D", "32E", "32F", "32G", "32G", "32H", "34G", "34H", "34I", "36I", "36J"],
        'charlene' : [0, "32E", "34E", "36F", "38H"],
        'hari' : [0, "28B", "28C", "28C", "28D", "30C", "30C", "30D", "32D"],
        'katrine' : [0, "34F", "34H", "34H", "34I", "34I", "34I", "36G", "36G", "36G", "36H", "40F"],
        'leanne' : [0, "30C", "32C", "32D", "32E", "32F", "32F", "32G", "32G", "32H", "34G", "34I", "42H", "42I", "42J", "46L"],
        'lisa' : [0, "34D", "34E", "34E", "36E", "36G", "38G", "40G", "40G", "40H", "40H", "40H", "44F"],
        'luna' : [0, "32D", "32E", "34E", "34G", "36H", "36H", "36J", "38J", "38L", "38N", "40O", "40Q"],
        'marie' : [0, "30B", "32B", "32B", "34B", "34B", "36B", "36C", "38A", "38B", "38C", "40A"],
        'maya' : [0, "34G", "34H", "34I", "36H", "36J", "36K", "38I", "38J", "38K", "38L", "40L"],
        'mylenna' : [0, "30E", "32E"],
        'natalie' : [0, "30C", "32F", "34H", "36N"],
        'rebecca' : [0, "34E", "34G", "34H"],
        'roxie' : [0, "30D", "30F", "32I", "34L"],
        'sally' : [0, "32D", "32G", "34I", "38J"],
        'daisy' : [0, "32D", "32D", "32E", "32E", "32E", "34D", "34D", "34D", "34E", "34E", "36C", "36D", "36D", "38C", "38C", "40C", "42D"],
        'trista' : [0, "32D", "32D", "32D", "32D", "32E", "32E", "32E", "32E", "32F", "34F", "36F", "38G", "40G"],
        'vicky' : [0, "34E", "34G", "36F", "38F", "38H"],
    }
    char_boobweight = {
        'amber' : [0],
        'bonnie' : [0],
        'britta' : [0, 0.5, 1.1, 2.3, 3.5],
        'caroline' : [0],
        'cayenne' : [0],
        'charlene' : [0, 1.0, 1.3, 1.8, 2.8],
        'hari' : [0],
        'katrine' : [0],
        'leanne' : [0],
        'lisa' : [0],
        'luna' : [0, 1.1, 1.3, 1.5, 1.8, 2.2, 2.7, 3.3, 3.7, 4.5, 5.5, 6.9, 7.5],
        'marie' : [0],
        'maya' : [0],
        'mylenna' : [0],
        'natalie' : [0, 0.55, 1.3, 2.5, 4.8],
        'rebecca' : [0],
        'roxie' : [0, 0.7, 1.2, 2.3, 3.7],
        'sally' : [0, 0.88, 1.4, 2.2, 3.6],
        'daisy' : [0, 0.8, 0.85, 0.9, 0.95, 1, 1.05, 1.1, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.6, 1.7, 1.8],
        'trista' : [0],
        'vicky' : [0],
    }
    char_lactation = {
        'amber' : [0],
        'bonnie' : [0],
        'britta' : [0, 0, 0, 0.8, 3],
        'caroline' : [0],
        'cayenne' : [0],
        'charlene' : [0],
        'hari' : [0],
        'katrine' : [0],
        'leanne' : [0],
        'lisa' : [0],
        'luna' : [0],
        'marie' : [0],
        'maya' : [0],
        'mylenna' : [0],
        'natalie' : [0, 0, 1.2, 3, 6],
        'rebecca' : [0],
        'roxie' : [0],
        'sally' : [0],
        'daisy' : [0],
        'trista' : [0],
        'vicky' : [0],
    }
    char_stomachcapacity = {
        'amber' : [0, 1.2, 1.3, 1.4, 1.5, 1.7, 2, 2.3, 2.6, 3, 3.5, 4.5, 5.5, 8],
        'bonnie' : [0, 1.3, 1.3, 1.4, 1.4, 1.5, 1.6, 1.8, 2.0, 2.5, 3.2, 4, 5, 6],
        'britta' : [0],
        'caroline' : [0],
        'cayenne' : [0, 1, 1.2, 1.5, 1.8, 2.2, 2.7, 2.7, 3, 3.5, 4, 4.8],
        'charlene' : [0],
        'hari' : [0],
        'katrine' : [0, 2, 2.1, 2.3, 2.5, 3, 3.3, 3.7, 3.8, 4, 4.5, 5],
        'leanne' : [0, 1, 1.1, 1.2, 1.3, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5, 2.7, 3.7, 4, 4.5, 5.5],
        'lisa' : [0, 1, 1.2, 1.5, 2, 2.5, 3, 3.5, 4, 4.2, 4.5, 4.7, 5.5],
        'luna' : [0, 1.2, 1.6, 1.9, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.5, 4, 4.2],
        'marie' : [0],
        'maya' : [0],
        'mylenna' : [0],
        'natalie' : [0],
        'rebecca' : [0],
        'roxie' : [0],
        'sally' : [0],
        'daisy' : [0, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.3, 2.5, 2.8, 3, 3.3, 3.6, 4, 4.4, 4.8, 5.2, 5.5],
        'trista' : [0, 1.4, 1.6, 1.8, 2, 2.4, 2.8, 3.5, 4.2, 5, 5.5, 6, 7, 8],
        'vicky' : [0],
    }
    char_leanweight = {
        'amber' : [0, 40.8, 40.9, 41.0, 41.1, 41.1, 41.0, 40.9, 40.8, 40.7, 40.5, 40.3, 40.2, 40.0],
        'bonnie' : [0, 50.2, 50.2, 50.2, 50.1, 50.1, 50.0, 49.9, 49.7, 49.5, 49.2, 48.8, 48.3, 48.1],
        'britta' : [0, 49.8, 49.7, 49.6, 49.5],
        'caroline' : [0, 61.2, 61.4, 61.6, 61.8, 62.0],
        'cayenne' : [0, 43.5, 43.7, 43.9, 44.1, 44.2, 44.3, 44.4, 44.5, 44.5, 44.5, 44.4],
        'charlene' : [0, 54.1, 53.6, 52.8, 51.4],
        'hari' : [0, 41.0, 41.2, 41.4, 41.6, 41.8, 42.0, 42.1, 41.8],
        'katrine' : [0, 62.8, 64.3, 65.3, 66.1, 67.0, 67.6, 68.0, 68.3, 68.5, 68.5, 68.3],
        'leanne' : [0, 46.7, 46.9, 47.1, 47.4, 47.8, 48.2, 48.6, 48.8, 49.0, 49.1, 49.2, 48.9, 48.8, 48.6, 48.4],
        'lisa' : [0, 41.1, 41.0, 40.9, 40.8, 40.7, 40.5, 40.3, 40.0, 39.7, 39.3, 39.0, 38.8],
        'luna' : [0, 43.1, 43.2, 43.3, 43.4, 43.4, 43.4, 43.3, 43.2, 43.0, 42.8, 42.5, 42.2],
        'marie' : [0, 51.1, 51.2, 51.3, 51.3, 51.1, 50.9, 50.7, 50.4, 50.1, 49.8, 49.5],
        'maya' : [0, 59.6, 59.6, 59.7, 59.9, 60.1, 60.2, 60.2, 60.1, 60.0, 59.8, 59.4],
        'mylenna' : [0, 48.4, 48.9],
        'natalie' : [0, 48.5, 48.4, 48.2, 47.8],
        'rebecca' : [0, 60.0, 60.6, 60.9],
        'roxie' : [0, 48.3, 48.2, 48.0, 47.7],
        'sally' : [0, 53.2, 52.9, 52.6, 52.1],
        'daisy' : [0, 40.2, 39.9, 39.7, 39.6, 39.5, 39.3, 39.1, 39.0, 38.9, 38.8, 38.7, 38.6, 38.5, 38.4, 38.3, 38.0, 37.8],
        'trista' : [0, 66.5, 68.8, 71.1, 73.2, 75.2, 76.9, 78.4, 80.0, 81.2, 81.8, 82.1, 82.3, 82.5],
        'vicky' : [0, 74.0, 74.5, 74.7, 74.9, 75.0],
    }


label weight_check:
    #this part changes the stats and stage based on weight.

    if bunnybitesgirlsstage2 == 1:
        if marie.stage == 2 or lisa.stage == 2 or amber.stage == 2:
            $ marie.weight = 65
            $ amber.weight = 53
            $ lisa.weight = 57
            $ bunnybitesgirlsstage2 = 0
    if bunnybitesgirlsstage3 == 1:
        if marie.weight >= 69 or lisa.weight >= 60 or amber.weight >= 57:
            $ mariestage3eventtrigger = 1
            $ marie.weight = 69
            $ amber.weight = 57
            $ lisa.weight = 60
            $ bunnybitesgirlsstage3 = 0


    #Roxie
    if roxie.stage == 4:
        $ roxie.weight = 79
        $ roxie.breast_cup = "34L"
        $ roxie.breast_size = 46.3
        $ roxie.breast_weight = 3.7
        $ roxie.ass_size = 43.8
        $ roxie.waist_size = 26.0
        $ roxie.leanweight = 47.7
    elif roxie.stage == 3:
        $ roxie.weight = 72
        $ roxie.breast_cup = "32I"
        $ roxie.breast_size = 41.4
        $ roxie.breast_weight = 2.3
        $ roxie.ass_size = 41.0
        $ roxie.waist_size = 24.3
        $ roxie.leanweight = 48.0
    elif roxie.stage == 2:
        $ roxie.weight = 65
        $ roxie.breast_cup = "30F"
        $ roxie.breast_size = 36.4
        $ roxie.breast_weight = 1.2
        $ roxie.ass_size = 38.3
        $ roxie.waist_size = 22.7
        $ roxie.leanweight = 48.2
    else:
        $ roxie.weight = 61
        $ roxie.breast_cup = "30D"
        $ roxie.breast_size = 33.8
        $ roxie.breast_weight = 0.7
        $ roxie.ass_size = 37.1
        $ roxie.waist_size = 22.2
        $ roxie.leanweight = 48.3


    #Charlene
    if charlene.stage == 4:
        $ charlene.weight = 118
        $ charlene.breast_cup = "38H"
        $ charlene.breast_size = 46.2
        $ charlene.breast_weight = 2.8
        $ charlene.ass_size = 49.6
        $ charlene.waist_size = 41.2
        $ charlene.leanweight = 51.4
    elif charlene.stage == 3:
        $ charlene.weight = 98
        $ charlene.breast_cup = "36F"
        $ charlene.breast_size = 41.9
        $ charlene.breast_weight = 1.8
        $ charlene.ass_size = 47.4
        $ charlene.waist_size = 36.1
        $ charlene.leanweight = 52.8
    elif charlene.stage == 2:
        $ charlene.weight = 86
        $ charlene.breast_cup = "34E"
        $ charlene.breast_size = 39.3
        $ charlene.breast_weight = 1.3
        $ charlene.ass_size = 42.6
        $ charlene.waist_size = 30.9
        $ charlene.leanweight = 53.6
    else:
        $ charlene.weight = 78
        $ charlene.breast_cup = "32E"
        $ charlene.breast_size = 37.2
        $ charlene.breast_weight = 1.0
        $ charlene.ass_size = 38.8
        $ charlene.waist_size = 26.2
        $ charlene.leanweight = 54.1

    #Sally
    if sally.stage == 4:
        $ sally.weight = 104
        $ sally.breast_cup = "38J"
        $ sally.breast_size = 48.1
        $ sally.breast_weight = 3.6
        $ sally.ass_size = 56.0
        $ sally.waist_size = 34.9
        $ sally.leanweight = 52.1
    elif sally.stage == 3:
        $ sally.weight = 90
        $ sally.breast_cup = "34I"
        $ sally.breast_size = 42.7
        $ sally.breast_weight = 2.2
        $ sally.ass_size = 50.1
        $ sally.waist_size = 31.0
        $ sally.leanweight = 52.6
    elif sally.stage == 2:
        $ sally.weight = 80
        $ sally.breast_cup = "32G"
        $ sally.breast_size = 39.0
        $ sally.breast_weight = 1.4
        $ sally.ass_size = 45.0
        $ sally.waist_size = 27.6
        $ sally.leanweight = 52.9
    else:
        $ sally.weight = 74
        $ sally.breast_cup = "32D"
        $ sally.breast_size = 35.6
        $ sally.breast_weight = 0.88
        $ sally.ass_size = 39.7
        $ sally.waist_size = 25.7
        $ sally.leanweight = 53.2

    #Natalie
    if natalie.stage == 4:
        $ natalie.weight = 90
        $ natalie.breast_cup = "36N"
        $ natalie.breast_size = 50.4
        $ natalie.breast_weight = 4.8
        $ natalie.ass_size = 49.0
        $ natalie.waist_size = 31.9
        $ natalie.lactation = 6
        $ natalie.leanweight = 47.8
    elif natalie.stage == 3:
        $ natalie.weight = 79
        $ natalie.breast_cup = "34H"
        $ natalie.breast_size = 42.4
        $ natalie.breast_weight = 2.5
        $ natalie.ass_size = 45.3
        $ natalie.waist_size = 25.8
        $ natalie.lactation = 3
        $ natalie.leanweight = 48.2
    elif natalie.stage >= 2:
        $ natalie.weight = 70
        $ natalie.breast_cup = "32F"
        $ natalie.breast_size = 38.2
        $ natalie.breast_weight = 1.3
        $ natalie.ass_size = 42.6
        $ natalie.waist_size = 24.3
        $ natalie.lactation = 1.2
        $ natalie.leanweight = 48.4
    else:
        $ natalie.weight = 64
        $ natalie.breast_cup = "30C"
        $ natalie.breast_size = 32.9
        $ natalie.breast_weight = 0.55
        $ natalie.ass_size = 41.5
        $ natalie.waist_size = 23.9
        $ natalie.leanweight = 48.5

    #Britta
    if britta.stage == 4:
        $ britta.weight = 87
        $ britta.breast_cup = "38I"
        $ britta.breast_size = 46.9
        $ britta.breast_weight = 3.5
        $ britta.ass_size = 45.0
        $ britta.waist_size = 29.2
        $ britta.lactation = 3
        $ britta.leanweight = 49.5
    elif britta.stage == 3:
        $ britta.weight = 78
        $ britta.breast_cup = "36H"
        $ britta.breast_size = 44.2
        $ britta.breast_weight = 2.3
        $ britta.ass_size = 43.1
        $ britta.waist_size = 28.0
        $ britta.lactation = 0.8
        $ britta.leanweight = 49.6
    elif britta.stage == 2:
        $ britta.weight = 72
        $ britta.breast_cup = "34D"
        $ britta.breast_size = 38.5
        $ britta.breast_weight = 1.3
        $ britta.ass_size = 41.9
        $ britta.waist_size = 27.3
        $ britta.leanweight = 49.7
    else:
        $ britta.weight = 68
        $ britta.breast_cup = "32B"
        $ britta.breast_size = 34.3
        $ britta.breast_weight = 0.5
        $ britta.ass_size = 41.5
        $ britta.waist_size = 27.0
        $ britta.leanweight = 49.8

    #Mylenna
    if mylenna.weight >= 63:
        $ mylenna.stage = 2
        $ mylenna.breast_cup = "32E"
        $ mylenna.breast_size = 37.3
        $ mylenna.ass_size = 38.1
        $ mylenna.waist_size = 23.3
        $ mylenna.leanweight = 48.9
    else:
        $ mylenna.stage = 1

    #Rebecca
    if rebecca.weight >= 93:
        $ rebecca.stage = 3
        $ rebecca.breast_cup = "34H"
        $ rebecca.breast_size = 42.2
        $ rebecca.ass_size = 49.3
        $ rebecca.waist_size = 29.2
        $ rebecca.leanweight = 60.9
    elif rebecca.weight >= 88:
        $ rebecca.stage = 2
        $ rebecca.breast_cup = "34G"
        $ rebecca.breast_size = 40.8
        $ rebecca.ass_size = 47.8
        $ rebecca.waist_size = 27.1
        $ rebecca.leanweight = 60.6
    else:
        $ rebecca.stage = 1

    #Vicky
    if vicky.weight >= 132:
        $ vicky.stage = 5
        $ vicky.breast_cup = "38H"
        $ vicky.breast_size = 45.9
        $ vicky.ass_size = 55.9
        $ vicky.waist_size = 36.0
        $ vicky.leanweight = 75.0
    elif vicky.weight >= 120:
        $ vicky.stage = 4
        $ vicky.breast_cup = "38F"
        $ vicky.breast_size = 44.4
        $ vicky.ass_size = 51.9
        $ vicky.waist_size = 34.1
        $ vicky.leanweight = 74.9
    elif vicky.weight >= 108:
        $ vicky.stage = 3
        $ vicky.breast_cup = "36F"
        $ vicky.breast_size = 42.0
        $ vicky.ass_size = 49.1
        $ vicky.waist_size = 32.1
        $ vicky.leanweight = 74.7
    elif vicky.weight >= 98:
        $ vicky.stage = 2
        $ vicky.breast_cup = "34G"
        $ vicky.breast_size = 41.2
        $ vicky.ass_size = 46.0
        $ vicky.waist_size = 29.7
        $ vicky.leanweight = 74.5
    else:
        $ vicky.stage = 1

    #Bonnie
    if bonnie.weight >= 142:
        $ bonnie.stage = 13
        $ bonnie.breast_cup = "42F"
        $ bonnie.breast_size = 47.9
        $ bonnie.ass_size = 65.4
        $ bonnie.waist_size = 47.0
        $ bonnie.stomach_capacity = 6
        $ bonnie.leanweight = 48.1
        $ librarianstage = 4
    elif bonnie.weight >= 130:
        $ bonnie.stage = 12
        $ bonnie.breast_cup = "42E"
        $ bonnie.breast_size = 46.6
        $ bonnie.ass_size = 62.2
        $ bonnie.waist_size = 43.4
        $ bonnie.stomach_capacity = 5
        $ bonnie.leanweight = 48.3
    elif bonnie.weight >= 120:
        $ bonnie.stage = 11
        $ bonnie.breast_cup = "40E"
        $ bonnie.breast_size = 45.4
        $ bonnie.ass_size = 59.6
        $ bonnie.waist_size = 40.3
        $ bonnie.stomach_capacity = 4
        $ bonnie.leanweight = 48.8
    elif bonnie.weight >= 111:
        $ bonnie.stage = 10
        $ bonnie.breast_cup = "38E"
        $ bonnie.breast_size = 44.0
        $ bonnie.ass_size = 57
        $ bonnie.waist_size = 38.3
        $ bonnie.stomach_capacity = 3.2
        $ bonnie.leanweight = 49.2
    elif bonnie.weight >= 103:
        $ bonnie.stage = 9
        $ bonnie.breast_cup = "38E"
        $ bonnie.breast_size = 42.8
        $ bonnie.ass_size = 54.7
        $ bonnie.waist_size = 34.9
        $ bonnie.stomach_capacity = 2.5
        $ bonnie.leanweight = 49.5
    elif bonnie.weight >= 96:
        $ bonnie.stage = 8
        $ bonnie.breast_cup = "36E"
        $ bonnie.breast_size = 41.4
        $ bonnie.ass_size = 53.1
        $ bonnie.waist_size = 33.6
        $ bonnie.stomach_capacity = 2.0
        $ bonnie.leanweight = 49.7
    elif bonnie.weight >= 90:
        $ bonnie.stage = 7
        $ bonnie.breast_cup = "36E"
        $ bonnie.breast_size = 40.3
        $ bonnie.ass_size = 50.6
        $ bonnie.waist_size = 30.0
        $ bonnie.stomach_capacity = 1.8
        $ bonnie.leanweight = 49.9
    elif bonnie.weight >= 86:
        $ bonnie.stage = 6
        $ bonnie.breast_cup = "34E"
        $ bonnie.breast_size = 39.7
        $ bonnie.ass_size = 48.7
        $ bonnie.waist_size = 29.6
        $ bonnie.stomach_capacity = 1.6
        $ bonnie.leanweight = 50.0
    elif bonnie.weight >= 82:
        $ bonnie.stage = 5
        $ bonnie.breast_cup = "34E"
        $ bonnie.breast_size = 39.1
        $ bonnie.ass_size = 47.4
        $ bonnie.waist_size = 28.3
        $ bonnie.stomach_capacity = 1.5
        $ bonnie.leanweight = 50.1
    elif bonnie.weight >= 79:
        $ bonnie.stage = 4
        $ bonnie.breast_cup = "34E"
        $ bonnie.breast_size = 38.4
        $ bonnie.ass_size = 46.2
        $ bonnie.waist_size = 27.4
        $ bonnie.stomach_capacity = 1.4
        $ bonnie.leanweight = 50.1
    elif bonnie.weight >= 76:
        $ bonnie.stage = 3
        $ bonnie.breast_cup = "32E"
        $ bonnie.breast_size = 37.7
        $ bonnie.ass_size = 45.2
        $ bonnie.waist_size = 26.7
        $ bonnie.stomach_capacity = 1.4
        $ bonnie.leanweight = 50.2
    elif bonnie.weight >= 73:
        $ bonnie.stage = 2
        $ bonnie.breast_cup = "32E"
        $ bonnie.breast_size = 36.7
        $ bonnie.ass_size = 43.8
        $ bonnie.waist_size = 25.7
        $ bonnie.stomach_capacity = 1.3
        $ bonnie.leanweight = 50.2
    else:
        $ bonnie.stage = 1

    #Marie
    #if marie.weight >= 150:
    #    $ marie.stage = 12
    #    $ marie.breast_cup = "48B"
    #    $ marie.breast_size = 50.0
    #    $ marie.ass_size = 60.6
    #    $ marie.waist_size = 58.3
    #    $ marie.leanweight = 49.2
    if marie.weight >= 122:
        $ marie.stage = 11
        $ marie.breast_cup = "40A"
        $ marie.breast_size = 41.2
        $ marie.ass_size = 53.8
        $ marie.waist_size = 47.3
        $ marie.leanweight = 49.5
    elif marie.weight >= 112:
        $ marie.stage = 10
        $ marie.breast_cup = "38C"
        $ marie.breast_size = 40.7
        $ marie.ass_size = 52.0
        $ marie.waist_size = 45.3
        $ marie.leanweight = 49.8
    elif marie.weight >= 104:
        $ marie.stage = 9
        $ marie.breast_cup = "38B"
        $ marie.breast_size = 40.2
        $ marie.ass_size = 50.8
        $ marie.waist_size = 43.9
        $ marie.leanweight = 50.1
    elif marie.weight >= 97:
        $ marie.stage = 8
        $ marie.breast_cup = "38A"
        $ marie.breast_size = 39.2
        $ marie.ass_size = 50.1
        $ marie.waist_size = 42.3
        $ marie.leanweight = 50.4
    elif marie.weight >= 91:
        $ marie.stage = 7
        $ marie.breast_cup = "36C"
        $ marie.breast_size = 38.6
        $ marie.ass_size = 48.9
        $ marie.waist_size = 41.0
        $ marie.leanweight = 50.7
    elif marie.weight >= 85:
        $ marie.stage = 6
        $ marie.breast_cup = "36B"
        $ marie.breast_size = 37.6
        $ marie.ass_size = 47.1
        $ marie.waist_size = 38.8
        $ marie.leanweight = 50.9
    elif marie.weight >= 79 and mariestage3event == 0:
        $ marie.stage = 5
        $ marie.breast_cup = "34B"
        $ marie.breast_size = 37.0
        $ marie.ass_size = 45.5
        $ marie.waist_size = 37.2
        $ marie.leanweight = 51.1
    elif marie.weight >= 74 and mariestage3event == 0:
        $ marie.stage = 4
        $ marie.breast_cup = "34B"
        $ marie.breast_size = 35.5
        $ marie.ass_size = 43.9
        $ marie.waist_size = 35.2
        $ marie.leanweight = 51.3
    elif marie.weight >= 69:
        $ marie.stage = 3
        $ marie.breast_cup = "32B"
        $ marie.breast_size = 34.8
        $ marie.ass_size = 42.0
        $ marie.waist_size = 33.0
        $ marie.leanweight = 51.3
    elif marie.weight >= 65:
        $ marie.stage = 2
        $ marie.breast_cup = "32B"
        $ marie.breast_size = 33.9
        $ marie.ass_size = 40.4
        $ marie.waist_size = 29.8
        $ marie.leanweight = 51.2
    else:
        $ marie.stage = 1

    #Lisa
    if lisa.weight >= 110:
        $ lisa.stage = 12
        $ lisa.breast_cup = "44F"
        $ lisa.breast_size = 49.9
        $ lisa.ass_size = 58.3
        $ lisa.waist_size = 42.7
        $ lisa.stomach_capacity = 5.5
        $ lisa.leanweight = 38.8
    elif lisa.weight >= 99:
        $ lisa.stage = 11
        $ lisa.breast_cup = "40H"
        $ lisa.breast_size = 48
        $ lisa.ass_size = 54.2
        $ lisa.waist_size = 40.4
        $ lisa.stomach_capacity = 4.7
        $ lisa.leanweight = 39.0
    elif lisa.weight >= 94:
        $ lisa.stage = 10
        $ lisa.breast_cup = "40H"
        $ lisa.breast_size = 47.9
        $ lisa.ass_size = 51.8
        $ lisa.waist_size = 38.2
        $ lisa.stomach_capacity = 4.5
        $ lisa.leanweight = 39.3
    elif lisa.weight >= 88:
        $ lisa.stage = 9
        $ lisa.breast_cup = "40H"
        $ lisa.breast_size = 47.8
        $ lisa.ass_size = 49.4
        $ lisa.waist_size = 35.7
        $ lisa.stomach_capacity = 4.2
        $ lisa.leanweight = 39.7
    elif lisa.weight >= 83:
        $ lisa.stage = 8
        $ lisa.breast_cup = "40G"
        $ lisa.breast_size = 47.3
        $ lisa.ass_size = 48.1
        $ lisa.waist_size = 34.5
        $ lisa.stomach_capacity = 4
        $ lisa.leanweight = 40.0
    elif lisa.weight >= 78:
        $ lisa.stage = 7
        $ lisa.breast_cup = "40G"
        $ lisa.breast_size = 46.9
        $ lisa.ass_size = 46.5
        $ lisa.waist_size = 33.1
        $ lisa.stomach_capacity = 3.5
        $ lisa.leanweight = 40.3
    elif lisa.weight >= 73:
        $ lisa.stage = 6
        $ lisa.breast_cup = "38G"
        $ lisa.breast_size = 44.7
        $ lisa.ass_size = 43.9
        $ lisa.waist_size = 31.7
        $ lisa.stomach_capacity = 3
        $ lisa.leanweight = 40.5
    elif lisa.weight >= 68 and mariestage3event == 0:
        $ lisa.stage = 5
        $ lisa.breast_cup = "36G"
        $ lisa.breast_size = 42.6
        $ lisa.ass_size = 41.7
        $ lisa.waist_size = 30.6
        $ lisa.stomach_capacity = 2.5
        $ lisa.leanweight = 40.7
    elif lisa.weight >= 64 and mariestage3event == 0:
        $ lisa.stage = 4
        $ lisa.breast_cup = "36E"
        $ lisa.breast_size = 40.7
        $ lisa.ass_size = 39.7
        $ lisa.waist_size = 29.6
        $ lisa.stomach_capacity = 2
        $ lisa.leanweight = 40.8
    elif lisa.weight >= 60:
        $ lisa.stage = 3
        $ lisa.breast_cup = "34E"
        $ lisa.breast_size = 40.4
        $ lisa.ass_size = 37.9
        $ lisa.waist_size = 27.5
        $ lisa.stomach_capacity = 1.5
        $ lisa.leanweight = 40.9
    elif lisa.weight >= 57:
        $ lisa.stage = 2
        $ lisa.breast_cup = "34E"
        $ lisa.breast_size = 39
        $ lisa.ass_size = 36.4
        $ lisa.waist_size = 26.1
        $ lisa.stomach_capacity = 1.2
        $ lisa.leanweight = 41.0
    else:
        $ lisa.stage = 1

    #Amber
    if amber.weight >= 145:
        $ amber.stage = 13
        $ amber.breast_cup = "50AA"
        $ amber.breast_size = 51.3
        $ amber.ass_size = 55.3
        $ amber.waist_size = 58.1
        $ amber.leanweight = 40.0
        $ amber.stomach_capacity = 8
    elif amber.weight >= 120:
        $ amber.stage = 12
        $ amber.breast_cup = "44AA"
        $ amber.breast_size = 42.9
        $ amber.ass_size = 51.0
        $ amber.waist_size = 50.8
        $ amber.leanweight = 40.2
        $ amber.stomach_capacity = 5.5
    elif amber.weight >= 110:
        $ amber.stage = 11
        $ amber.breast_cup = "40AA"
        $ amber.breast_size = 40.3
        $ amber.ass_size = 49.5
        $ amber.waist_size = 46.9
        $ amber.leanweight = 40.3
        $ amber.stomach_capacity = 4.5
    elif amber.weight >= 101:
        $ amber.stage = 10
        $ amber.breast_cup = "38A"
        $ amber.breast_size = 39.4
        $ amber.ass_size = 48.1
        $ amber.waist_size = 44.6
        $ amber.leanweight = 40.5
        $ amber.stomach_capacity = 3.5
    elif amber.weight >= 93:
        $ amber.stage = 9
        $ amber.breast_cup = "38A"
        $ amber.breast_size = 38.8
        $ amber.ass_size = 47.4
        $ amber.waist_size = 42.4
        $ amber.leanweight = 40.7
        $ amber.stomach_capacity = 3
    elif amber.weight >= 85:
        $ amber.stage = 8
        $ amber.breast_cup = "36B"
        $ amber.breast_size = 38.0
        $ amber.ass_size = 46.8
        $ amber.waist_size = 40.7
        $ amber.leanweight = 40.8
        $ amber.stomach_capacity = 2.6
    elif amber.weight >= 78:
        $ amber.stage = 7
        $ amber.breast_cup = "36A"
        $ amber.breast_size = 36.6
        $ amber.ass_size = 45.1
        $ amber.waist_size = 39.1
        $ amber.leanweight = 40.9
        $ amber.stomach_capacity = 2.3
    elif amber.weight >= 72:
        $ amber.stage = 6
        $ amber.breast_cup = "34B"
        $ amber.breast_size = 36.2
        $ amber.ass_size = 43.8
        $ amber.waist_size = 37.6
        $ amber.leanweight = 41.0
        $ amber.stomach_capacity = 2
    elif amber.weight >= 66 and mariestage3event == 0:
        $ amber.stage = 5
        $ amber.breast_cup = "34B"
        $ amber.breast_size = 35.7
        $ amber.ass_size = 41.7
        $ amber.waist_size = 35.4
        $ amber.leanweight = 41.1
        $ amber.stomach_capacity = 1.7
    elif amber.weight >= 61 and mariestage3event == 0:
        $ amber.stage = 4
        $ amber.breast_cup = "32C"
        $ amber.breast_size = 35.2
        $ amber.ass_size = 41.7
        $ amber.waist_size = 32.5
        $ amber.leanweight = 41.1
        $ amber.stomach_capacity = 1.5
    elif amber.weight >= 57:
        $ amber.stage = 3
        $ amber.breast_cup = "32C"
        $ amber.breast_size = 34.9
        $ amber.ass_size = 38.9
        $ amber.waist_size = 29.6
        $ amber.leanweight = 41.0
        $ amber.stomach_capacity = 1.4
    elif amber.weight >= 53:
        $ amber.stage = 2
        $ amber.breast_cup = "32C"
        $ amber.breast_size = 34.9
        $ amber.ass_size = 38.8
        $ amber.waist_size = 28.9
        $ amber.leanweight = 40.9
        $ amber.stomach_capacity = 1.3
    else:
        $ amber.stage = 1

    #Cayenne
    if cayenne.weight >= 93:
        $ cayenne.stage = 11
        $ cayenne.breast_cup = "36J"
        $ cayenne.breast_size = 45.9
        $ cayenne.ass_size = 50.1
        $ cayenne.waist_size = 35.4
        $ cayenne.stomach_capacity = 4.8
        $ cayenne.leanweight = 44.4
    elif cayenne.weight >= 87:
        $ cayenne.stage = 10
        $ cayenne.breast_cup = "36I"
        $ cayenne.breast_size = 44.5
        $ cayenne.ass_size = 48.2
        $ cayenne.waist_size = 33.3
        $ cayenne.stomach_capacity = 4
        $ cayenne.leanweight = 44.5
    elif cayenne.weight >= 82:
        $ cayenne.stage = 9
        $ cayenne.breast_cup = "34I"
        $ cayenne.breast_size = 43.4
        $ cayenne.ass_size = 46.7
        $ cayenne.waist_size = 31.6
        $ cayenne.stomach_capacity = 3.5
        $ cayenne.leanweight = 44.5
    elif cayenne.weight >= 77:
        $ cayenne.stage = 8
        $ cayenne.breast_cup = "34H"
        $ cayenne.breast_size = 42.4
        $ cayenne.ass_size = 45.4
        $ cayenne.waist_size = 30.3
        $ cayenne.stomach_capacity = 3
        $ cayenne.leanweight = 44.5
    elif cayenne.weight >= 73:
        $ cayenne.stage = 7
        $ cayenne.breast_cup = "34G"
        $ cayenne.breast_size = 40.8
        $ cayenne.ass_size = 43.8
        $ cayenne.waist_size = 29.4
        $ cayenne.stomach_capacity = 2.7
        $ cayenne.leanweight = 44.4
    elif cayenne.weight >= 70:
        $ cayenne.stage = 6
        $ cayenne.breast_cup = "32H"
        $ cayenne.breast_size = 40.0
        $ cayenne.ass_size = 42.3
        $ cayenne.waist_size = 28.6
        $ cayenne.stomach_capacity = 2.7
        $ cayenne.leanweight = 44.3
    elif cayenne.weight >= 65:
        $ cayenne.stage = 5
        $ cayenne.breast_cup = "32G"
        $ cayenne.breast_size = 39.3
        $ cayenne.ass_size = 41.0
        $ cayenne.waist_size = 27.9
        $ cayenne.stomach_capacity = 2.2
        $ cayenne.leanweight = 44.2
    elif cayenne.weight >= 60:
        $ cayenne.stage = 4
        $ cayenne.breast_cup = "32G"
        $ cayenne.breast_size = 38.6
        $ cayenne.ass_size = 39.8
        $ cayenne.waist_size = 27.3
        $ cayenne.stomach_capacity = 1.8
        $ cayenne.leanweight = 44.1
    elif cayenne.weight >= 56:
        $ cayenne.stage = 3
        $ cayenne.breast_cup = "32F"
        $ cayenne.breast_size = 37.8
        $ cayenne.ass_size = 38.6
        $ cayenne.waist_size = 26.6
        $ cayenne.stomach_capacity = 1.5
        $ cayenne.leanweight = 43.9
    elif cayenne.weight >= 53:
        $ cayenne.stage = 2
        $ cayenne.breast_cup = "32E"
        $ cayenne.breast_size = 37.0
        $ cayenne.ass_size = 37.0
        $ cayenne.waist_size = 25.7
        $ cayenne.stomach_capacity = 1.2
        $ cayenne.leanweight = 43.7
    else:
        $ cayenne.stage = 1

    if katrine.weight >= 136 and katrinestage1event == 0:
        $ katrine.stage = 11
        $ katrine.breast_cup = "40F"
        $ katrine.breast_size = 46.4
        $ katrine.ass_size = 59.1
        $ katrine.waist_size = 50.4
        $ katrine.stomach_capacity = 5
        $ katrine.leanweight = 68.3
    elif katrine.weight >= 126 and katrinestage1event == 0:
        $ katrine.stage = 10
        $ katrine.breast_cup = "36H"
        $ katrine.breast_size = 43.6
        $ katrine.ass_size = 57.2
        $ katrine.waist_size = 45.8
        $ katrine.stomach_capacity = 4.5
        $ katrine.leanweight = 68.5
    elif katrine.weight >= 120 and katrinestage1event == 0:
        $ katrine.stage = 9
        $ katrine.breast_cup = "36G"
        $ katrine.breast_size = 42.9
        $ katrine.ass_size = 55.0
        $ katrine.waist_size = 43.0
        $ katrine.stomach_capacity = 4
        $ katrine.leanweight = 68.5
    elif katrine.weight >= 114 and katrinestage1event == 0:
        $ katrine.stage = 8
        $ katrine.breast_cup = "36G"
        $ katrine.breast_size = 42.9
        $ katrine.ass_size = 54.0
        $ katrine.waist_size = 40.6
        $ katrine.stomach_capacity = 3.8
        $ katrine.leanweight = 68.3
    elif katrine.weight >= 108 and katrinestage1event == 0:
        $ katrine.stage = 7
        $ katrine.breast_cup = "36G"
        $ katrine.breast_size = 42.8
        $ katrine.ass_size = 52.7
        $ katrine.waist_size = 38.5
        $ katrine.stomach_capacity = 3.7
        $ katrine.leanweight = 68.0
    elif katrine.weight >= 102 and katrinestage1event == 0:
        $ katrine.stage = 6
        $ katrine.breast_cup = "34I"
        $ katrine.breast_size = 42.7
        $ katrine.ass_size = 52.2
        $ katrine.waist_size = 36.3
        $ katrine.stomach_capacity = 3.3
        $ katrine.leanweight = 67.6
    elif katrine.weight >= 97 and katrinestage1event == 0:
        $ katrine.stage = 5
        $ katrine.breast_cup = "34I"
        $ katrine.breast_size = 42.7
        $ katrine.ass_size = 50.4
        $ katrine.waist_size = 34.3
        $ katrine.stomach_capacity = 3
        $ katrine.leanweight = 67.0
    elif katrine.weight >= 92 and katrinestage1event == 0:
        $ katrine.stage = 4
        $ katrine.breast_cup = "34I"
        $ katrine.breast_size = 42.4
        $ katrine.ass_size = 49.6
        $ katrine.waist_size = 33.4
        $ katrine.stomach_capacity = 2.5
        $ katrine.leanweight = 66.1
    elif katrine.weight >= 88 and katrinestage1event == 0:
        $ katrine.stage = 3
        $ katrine.breast_cup = "34H"
        $ katrine.breast_size = 42.0
        $ katrine.ass_size = 48.2
        $ katrine.waist_size = 31.8
        $ katrine.stomach_capacity = 2.3
        $ katrine.leanweight = 65.3
    elif katrine.weight >= 84 and katrinestage1event == 0:
        $ katrine.stage = 2
        $ katrine.breast_cup = "34H"
        $ katrine.breast_size = 41.7
        $ katrine.ass_size = 45.8
        $ katrine.waist_size = 30.3
        $ katrine.stomach_capacity = 2.1
        $ katrine.leanweight = 64.3

    #Luna
    if luna.weight >= 108 and teacherstage14event == 0:
        $ luna.stage = 12
        $ luna.breast_weight = 7.5
        $ luna.breast_cup = "40Q"
        $ luna.breast_size = 56.2
        $ luna.ass_size = 50.4
        $ luna.waist_size = 38.6
        $ luna.stomach_capacity = 4.2
        $ luna.leanweight = 42.2
    elif luna.weight >= 101 and teacherstage14event == 0:
        $ luna.stage = 11
        $ luna.breast_weight = 6.9
        $ luna.breast_cup = "40O"
        $ luna.breast_size = 54.5
        $ luna.ass_size = 49.2
        $ luna.waist_size = 37.3
        $ luna.stomach_capacity = 4
        $ luna.leanweight = 42.5
    elif luna.weight >= 95:
        $ luna.stage = 10
        $ luna.breast_weight = 5.5
        $ luna.breast_cup = "38N"
        $ luna.breast_size = 52.3
        $ luna.ass_size = 48.0
        $ luna.waist_size = 36.9
        $ luna.stomach_capacity = 3.5
        $ luna.leanweight = 42.8
    elif luna.weight >= 90:
        $ luna.stage = 9
        $ luna.breast_weight = 4.5
        $ luna.breast_cup = "38L"
        $ luna.breast_size = 50.3
        $ luna.ass_size = 46.7
        $ luna.waist_size = 35.7
        $ luna.stomach_capacity = 3.2
        $ luna.leanweight = 43.0
    elif luna.weight >= 85:
        $ luna.stage = 8
        $ luna.breast_weight = 3.7
        $ luna.breast_cup = "38J"
        $ luna.breast_size = 48.1
        $ luna.ass_size = 45.3
        $ luna.waist_size = 34.3
        $ luna.stomach_capacity = 3
        $ luna.leanweight = 43.2
    elif luna.weight >= 80:
        $ luna.stage = 7
        $ luna.breast_weight = 3.3
        $ luna.breast_cup = "36J"
        $ luna.breast_size = 45.8
        $ luna.ass_size = 44.3
        $ luna.waist_size = 33.0
        $ luna.stomach_capacity = 2.8
        $ luna.leanweight = 43.3
    elif luna.weight >= 76:
        $ luna.stage = 6
        $ luna.breast_weight = 2.7
        $ luna.breast_cup = "36H"
        $ luna.breast_size = 44.4
        $ luna.ass_size = 43.1
        $ luna.waist_size = 31.2
        $ luna.stomach_capacity = 2.6
        $ luna.leanweight = 43.4
    elif luna.weight >= 71:
        $ luna.stage = 5
        $ luna.breast_weight = 2.2
        $ luna.breast_cup = "36H"
        $ luna.breast_size = 43.1
        $ luna.ass_size = 42.5
        $ luna.waist_size = 30.3
        $ luna.stomach_capacity = 2.4
        $ luna.leanweight = 43.4
    elif luna.weight >= 66:
        $ luna.stage = 4
        $ luna.breast_weight = 1.8
        $ luna.breast_cup = "34G"
        $ luna.breast_size = 40.5
        $ luna.ass_size = 40.8
        $ luna.waist_size = 28.6
        $ luna.stomach_capacity = 2.2
        $ luna.leanweight = 43.4
    elif luna.weight >= 62:
        $ luna.stage = 3
        $ luna.breast_weight = 1.5
        $ luna.breast_cup = "34E"
        $ luna.breast_size = 38.9
        $ luna.ass_size = 39.6
        $ luna.waist_size = 27.3
        $ luna.stomach_capacity = 1.9
        $ luna.leanweight = 43.3
    elif luna.weight >= 58:
        $ luna.stage = 2
        $ luna.breast_weight = 1.3
        $ luna.breast_cup = "32E"
        $ luna.breast_size = 37.5
        $ luna.ass_size = 38.3
        $ luna.waist_size = 25.8
        $ luna.stomach_capacity = 1.6
        $ luna.leanweight = 43.2
    else:
        $ luna.stage = 1

    #Trista
    if trista.weight >= 158:
        $ trista.stage = 13
        $ trista.breast_cup = "40G"
        $ trista.breast_size = 47.9
        $ trista.ass_size = 63.9
        $ trista.waist_size = 48.4
        $ trista.stomach_capacity = 8
        $ trista.leanweight = 82.5
    elif trista.weight >= 138:
        $ trista.stage = 12
        $ trista.breast_cup = "38G"
        $ trista.breast_size = 44.7
        $ trista.ass_size = 58.9
        $ trista.waist_size = 42.3
        $ trista.stomach_capacity = 7
        $ trista.leanweight = 82.3
    elif trista.weight >= 124:
        $ trista.stage = 11
        $ trista.breast_cup = "36F"
        $ trista.breast_size = 39.9
        $ trista.ass_size = 54.9
        $ trista.waist_size = 37.6
        $ trista.stomach_capacity = 6
        $ trista.leanweight = 82.1
    elif trista.weight >= 115:
        $ trista.stage = 10
        $ trista.breast_cup = "34F"
        $ trista.breast_size = 38.9
        $ trista.ass_size = 53.8
        $ trista.waist_size = 32.6
        $ trista.stomach_capacity = 5.5
        $ trista.leanweight = 81.8
    elif trista.weight >= 110:
        $ trista.stage = 9
        $ trista.breast_cup = "32F"
        $ trista.breast_size = 37.7
        $ trista.ass_size = 53.1
        $ trista.waist_size = 30.6
        $ trista.stomach_capacity = 5
        $ trista.leanweight = 81.2
    elif trista.weight >= 106:
        $ trista.stage = 8
        $ trista.breast_cup = "32E"
        $ trista.breast_size = 37.4
        $ trista.ass_size = 51.7
        $ trista.waist_size = 29.7
        $ trista.stomach_capacity = 4.2
        $ trista.leanweight = 80.0
    elif trista.weight >= 102:
        $ trista.stage = 7
        $ trista.breast_cup = "32E"
        $ trista.breast_size = 37.2
        $ trista.ass_size = 50.4
        $ trista.waist_size = 29.0
        $ trista.stomach_capacity = 3.5
        $ trista.leanweight = 78.4
    elif trista.weight >= 98:
        $ trista.stage = 6
        $ trista.breast_cup = "32E"
        $ trista.breast_size = 36.9
        $ trista.ass_size = 49.0
        $ trista.waist_size = 28.2
        $ trista.stomach_capacity = 2.8
        $ trista.leanweight = 76.9
    elif trista.weight >= 94:
        $ trista.stage = 5
        $ trista.breast_cup = "32E"
        $ trista.breast_size = 36.7
        $ trista.ass_size = 48.0
        $ trista.waist_size = 27.8
        $ trista.stomach_capacity = 2.4
        $ trista.leanweight = 75.2
    elif trista.weight >= 90:
        $ trista.stage = 4
        $ trista.breast_cup = "32D"
        $ trista.breast_size = 36.5
        $ trista.ass_size = 46.7
        $ trista.waist_size = 27.0
        $ trista.stomach_capacity = 2
        $ trista.leanweight = 73.2
    elif trista.weight >= 86:
        $ trista.stage = 3
        $ trista.breast_cup = "32D"
        $ trista.breast_size = 36.2
        $ trista.ass_size = 45.4
        $ trista.waist_size = 26.3
        $ trista.stomach_capacity = 1.8
        $ trista.leanweight = 71.1
    elif trista.weight >= 82:
        $ trista.stage = 2
        $ trista.breast_cup = "32D"
        $ trista.breast_size = 36.0
        $ trista.ass_size = 44.0
        $ trista.waist_size = 25.4
        $ trista.stomach_capacity = 1.6
        $ trista.leanweight = 68.8
    else:
        $ trista.stage = 1

    #Maya
    if maya.weight >= 130:
        $ maya.stage = 11
        $ maya.breast_cup = "40L"
        $ maya.breast_size = 51.7
        $ maya.ass_size = 52.4
        $ maya.waist_size = 39.9
        $ maya.leanweight = 59.4
    elif maya.weight >= 123:
        $ maya.stage = 10
        $ maya.breast_cup = "38L"
        $ maya.breast_size = 50.2
        $ maya.ass_size = 50.2
        $ maya.waist_size = 37.5
        $ maya.leanweight = 59.8
    elif maya.weight >= 116:
        $ maya.stage = 9
        $ maya.breast_cup = "38K"
        $ maya.breast_size = 49.0
        $ maya.ass_size = 48.9
        $ maya.waist_size = 35.2
        $ maya.leanweight = 60.0
    elif maya.weight >= 109:
        $ maya.stage = 8
        $ maya.breast_cup = "38J"
        $ maya.breast_size = 48.0
        $ maya.ass_size = 47.6
        $ maya.waist_size = 33.3
        $ maya.leanweight = 60.1
    elif maya.weight >= 103:
        $ maya.stage = 7
        $ maya.breast_cup = "38I"
        $ maya.breast_size = 46.8
        $ maya.ass_size = 46.3
        $ maya.waist_size = 31.7
        $ maya.leanweight = 60.2
    elif maya.weight >= 98:
        $ maya.stage = 6
        $ maya.breast_cup = "36K"
        $ maya.breast_size = 46.6
        $ maya.ass_size = 45.9
        $ maya.waist_size = 30.8
        $ maya.leanweight = 60.2
    elif maya.weight >= 93:
        $ maya.stage = 5
        $ maya.breast_cup = "36J"
        $ maya.breast_size = 45.5
        $ maya.ass_size = 44.7
        $ maya.waist_size = 29.5
        $ maya.leanweight = 60.1
    elif maya.weight >= 88:
        $ maya.stage = 4
        $ maya.breast_cup = "36H"
        $ maya.breast_size = 44.4
        $ maya.ass_size = 43.5
        $ maya.waist_size = 28.1
        $ maya.leanweight = 59.9
    elif maya.weight >= 84:
        $ maya.stage = 3
        $ maya.breast_cup = "34I"
        $ maya.breast_size = 43.4
        $ maya.ass_size = 42.5
        $ maya.waist_size = 27.0
        $ maya.leanweight = 59.7
    elif maya.weight >= 80:
        $ maya.stage = 2
        $ maya.breast_cup = "34H"
        $ maya.breast_size = 42.3
        $ maya.ass_size = 41.5
        $ maya.waist_size = 25.9
        $ maya.leanweight = 59.6
    else:
        $ maya.stage = 1

    #Caroline
    #if caroline.weight >= 90:
    #    $ caroline.stage = 5
    #    $ caroline.breast_cup = "34G"
    #    $ caroline.breast_size = 41.9
    #    $ caroline.ass_size = 40.9
    #    $ caroline.waist_size = 30.6
    #    $ caroline.leanweight = 62.0
    if caroline.weight >= 86:
        $ caroline.stage = 4
        $ caroline.breast_cup = "34G"
        $ caroline.breast_size = 40.8
        $ caroline.ass_size = 40.6
        $ caroline.waist_size = 29.6
        $ caroline.leanweight = 61.8
    elif caroline.weight >= 82:
        $ caroline.stage = 3
        $ caroline.breast_cup = "34E"
        $ caroline.breast_size = 39.1
        $ caroline.ass_size = 40.4
        $ caroline.waist_size = 28.2
        $ caroline.leanweight = 61.6
    elif caroline.weight >= 79:
        $ caroline.stage = 2
        $ caroline.breast_cup = "34D"
        $ caroline.breast_size = 36.9
        $ caroline.ass_size = 40.1
        $ caroline.waist_size = 25.8
        $ caroline.leanweight = 61.4
    else:
        $ caroline.stage = 1

    #Leanne
    if leanne.weight >= 152:
        $ leanne.stage = 15
        $ leanne.breast_cup = "46L"
        $ leanne.breast_size = 58.4
        $ leanne.ass_size = 64.1
        $ leanne.waist_size = 56.5
        $ leanne.stomach_capacity = 5.5
        $ leanne.leanweight = 48.4
    elif leanne.weight >= 132:
        $ leanne.stage = 14
        $ leanne.breast_cup = "42J"
        $ leanne.breast_size = 52.3
        $ leanne.ass_size = 59.3
        $ leanne.waist_size = 49.1
        $ leanne.stomach_capacity = 4.5
        $ leanne.leanweight = 48.6
    elif leanne.weight >= 123:
        $ leanne.stage = 13
        $ leanne.breast_cup = "42I"
        $ leanne.breast_size = 51.2
        $ leanne.ass_size = 59.1
        $ leanne.waist_size = 46.9
        $ leanne.stomach_capacity = 4
        $ leanne.leanweight = 48.8
    elif leanne.weight >= 116:
        $ leanne.stage = 12
        $ leanne.breast_cup = "42H"
        $ leanne.breast_size = 50.5
        $ leanne.ass_size = 57.3
        $ leanne.waist_size = 44.6
        $ leanne.stomach_capacity = 3.7
        $ leanne.leanweight = 48.9
    elif leanne.weight >= 92:
        $ leanne.stage = 11
        $ leanne.breast_weight = 1.6
        $ leanne.breast_cup = "34I"
        $ leanne.breast_size = 42.7
        $ leanne.ass_size = 45.9
        $ leanne.waist_size = 33.1
        $ leanne.stomach_capacity = 2.7
        $ leanne.leanweight = 49.2
    elif leanne.weight >= 87:
        $ leanne.stage = 10
        $ leanne.breast_weight = 1.5
        $ leanne.breast_cup = "34G"
        $ leanne.breast_size = 41.2
        $ leanne.ass_size = 45.0
        $ leanne.waist_size = 32.2
        $ leanne.stomach_capacity = 2.5
        $ leanne.leanweight = 49.1
    elif leanne.weight >= 82:
        $ leanne.stage = 9
        $ leanne.breast_weight = 1.4
        $ leanne.breast_cup = "32H"
        $ leanne.breast_size = 40.0
        $ leanne.ass_size = 44.0
        $ leanne.waist_size = 31.2
        $ leanne.stomach_capacity = 2.3
        $ leanne.leanweight = 49.0
    elif leanne.weight >= 78:
        $ leanne.stage = 8
        $ leanne.breast_weight = 1.3
        $ leanne.breast_cup = "32G"
        $ leanne.breast_size = 39.5
        $ leanne.ass_size = 43.1
        $ leanne.waist_size = 30.4
        $ leanne.stomach_capacity = 2.1
        $ leanne.leanweight = 48.8
    elif leanne.weight >= 74:
        $ leanne.stage = 7
        $ leanne.breast_weight = 1.2
        $ leanne.breast_cup = "32G"
        $ leanne.breast_size = 39.1
        $ leanne.ass_size = 42.3
        $ leanne.waist_size = 29.8
        $ leanne.stomach_capacity = 1.9
        $ leanne.leanweight = 48.6
    elif leanne.weight >= 70:
        $ leanne.stage = 6
        $ leanne.breast_weight = 1.1
        $ leanne.breast_cup = "32F"
        $ leanne.breast_size = 38.4
        $ leanne.ass_size = 41.5
        $ leanne.waist_size = 29.5
        $ leanne.stomach_capacity = 1.7
        $ leanne.leanweight = 48.2
    elif leanne.weight >= 66:
        $ leanne.stage = 5
        $ leanne.breast_weight = 1.0
        $ leanne.breast_cup = "32F"
        $ leanne.breast_size = 37.8
        $ leanne.ass_size = 40.5
        $ leanne.waist_size = 28.8
        $ leanne.stomach_capacity = 1.5
        $ leanne.leanweight = 47.8
    elif leanne.weight >= 62 and leannestage3event == 0:
        $ leanne.stage = 4
        $ leanne.breast_weight = 0.9
        $ leanne.breast_cup = "32E"
        $ leanne.breast_size = 36.9
        $ leanne.ass_size = 38.9
        $ leanne.waist_size = 27.0
        $ leanne.stomach_capacity = 1.3
        $ leanne.leanweight = 47.4
    elif leanne.weight >= 58 and leannestage2event2 == 0:
        $ leanne.stage = 3
        $ leanne.breast_weight = 0.8
        $ leanne.breast_cup = "32D"
        $ leanne.breast_size = 36.0
        $ leanne.ass_size = 37.3
        $ leanne.waist_size = 25.7
        $ leanne.stomach_capacity = 1.2
        $ leanne.leanweight = 47.1
    elif leanne.weight >= 55:
        $ leanne.stage = 2
        $ leanne.breast_weight = 0.7
        $ leanne.breast_cup = "32C"
        $ leanne.breast_size = 35.2
        $ leanne.ass_size = 36.3
        $ leanne.waist_size = 24.8
        $ leanne.stomach_capacity = 1.1
        $ leanne.leanweight = 46.9
    else:
        $ leanne.stage = 1

    #Hari
    if hari.weight >= 96 and haristage3event2 == 0:
        $ hari.stage = 8
        $ hari.breast_cup = "32D"
        $ hari.breast_size = 36.9
        $ hari.ass_size = 56.5
        $ hari.waist_size = 39.7
        $ hari.leanweight = 41.8
    elif hari.weight >= 84 and haristage3event2 == 0:
        $ hari.stage = 7
        $ hari.breast_cup = "30D"
        $ hari.breast_size = 34.4
        $ hari.ass_size = 53.8
        $ hari.waist_size = 34.0
        $ hari.leanweight = 42.1
    elif hari.weight >= 77 and haristage3event2 == 0:
        $ hari.stage = 6
        $ hari.breast_cup = "30C"
        $ hari.breast_size = 33.4
        $ hari.ass_size = 50.5
        $ hari.waist_size = 31.6
        $ hari.leanweight = 42.0
    elif hari.weight >= 69 and haristage3event2 == 0:
        $ hari.stage = 5
        $ hari.breast_cup = "30C"
        $ hari.breast_size = 32.9
        $ hari.ass_size = 49.3
        $ hari.waist_size = 30.4
        $ hari.leanweight = 41.8
    elif hari.weight >= 61 and haristage3event2 == 0:
        $ hari.stage = 4
        $ hari.breast_cup = "28D"
        $ hari.breast_size = 31.7
        $ hari.ass_size = 47.5
        $ hari.waist_size = 27.8
        $ hari.leanweight = 41.6
    elif hari.weight >= 55:
        $ hari.stage = 3
        $ hari.breast_cup = "28C"
        $ hari.breast_size = 30.8
        $ hari.ass_size = 43.9
        $ hari.waist_size = 25.0
        $ hari.leanweight = 41.4
    elif hari.weight >= 50:
        $ hari.stage = 2
        $ hari.breast_cup = "28C"
        $ hari.breast_size = 30.6
        $ hari.ass_size = 42.6
        $ hari.waist_size = 23.4
        $ hari.leanweight = 41.2
    else:
        $ hari.stage = 1

    #Daisy
    if teacher.weight >= 130 and teacherstage14event == 0:
        $ teacher.stage = 17
        $ teacher.breast_weight = 1.8
        $ teacher.breast_cup = "42D"
        $ teacher.breast_size = 45.8
        $ teacher.ass_size = 56.0
        $ teacher.waist_size = 53.6
        $ teacher.stomach_capacity = 5.5
        $ teacher.leanweight = 37.8
        return
    elif teacher.weight >= 120 and teacherstage14event == 0:
        $ teacher.stage = 16
        $ teacher.breast_weight = 1.7
        $ teacher.breast_cup = "40C"
        $ teacher.breast_size = 42.8
        $ teacher.ass_size = 51.9
        $ teacher.waist_size = 50.0
        $ teacher.stomach_capacity = 5.2
        $ teacher.leanweight = 38.0
        return
    elif teacher.weight >= 112 and teacherstage14event == 0:
        $ teacher.stage = 15
        $ teacher.breast_weight = 1.6
        $ teacher.breast_cup = "38C"
        $ teacher.breast_size = 41.4
        $ teacher.ass_size = 50.6
        $ teacher.waist_size = 46.9
        $ teacher.stomach_capacity = 4.8
        $ teacher.leanweight = 38.3
        return
    elif teacher.weight >= 106:
        $ teacher.stage = 14
        $ teacher.breast_weight = 1.5
        $ teacher.breast_cup = "38C"
        $ teacher.breast_size = 40.6
        $ teacher.ass_size = 49.1
        $ teacher.waist_size = 45.3
        $ teacher.stomach_capacity = 4.4
        $ teacher.leanweight = 38.4
        return
    elif teacher.weight >= 100:
        $ teacher.stage = 13
        $ teacher.breast_weight = 1.45
        $ teacher.breast_cup = "36D"
        $ teacher.breast_size = 39.8
        $ teacher.ass_size = 47.7
        $ teacher.waist_size = 43.6
        $ teacher.stomach_capacity = 4
        $ teacher.leanweight = 38.5
        return
    elif teacher.weight >= 95:
        $ teacher.stage = 12
        $ teacher.breast_weight = 1.40
        $ teacher.breast_cup = "36D"
        $ teacher.breast_size = 39.7
        $ teacher.ass_size = 46.2
        $ teacher.waist_size = 41.7
        $ teacher.stomach_capacity = 3.6
        $ teacher.leanweight = 38.6
        return
    elif teacher.weight >= 91:
        $ teacher.stage = 11
        $ teacher.breast_weight = 1.35
        $ teacher.breast_cup = "36C"
        $ teacher.breast_size = 39.4
        $ teacher.ass_size = 45.7
        $ teacher.waist_size = 40.4
        $ teacher.stomach_capacity = 3.3
        $ teacher.leanweight = 38.7
        return
    elif teacher.weight >= 86:
        $ teacher.stage = 10
        $ teacher.breast_weight = 1.3
        $ teacher.breast_cup = "34E"
        $ teacher.breast_size = 38.8
        $ teacher.ass_size = 44.4
        $ teacher.waist_size = 37.0
        $ teacher.stomach_capacity = 3
        $ teacher.leanweight = 38.8
        return
    elif teacher.weight >= 82:
        $ teacher.stage = 9
        $ teacher.breast_weight = 1.25
        $ teacher.breast_cup = "34E"
        $ teacher.breast_size = 38.7
        $ teacher.ass_size = 43.8
        $ teacher.waist_size = 35.7
        $ teacher.stomach_capacity = 2.8
        $ teacher.leanweight = 38.9
        return
    elif teacher.weight >= 77:
        $ teacher.stage = 8
        $ teacher.breast_weight = 1.2
        $ teacher.breast_cup = "34D"
        $ teacher.breast_size = 38.2
        $ teacher.ass_size = 42.9
        $ teacher.waist_size = 34.0
        $ teacher.stomach_capacity = 2.5
        $ teacher.leanweight = 39.0
        return
    elif teacher.weight >= 72:
        $ teacher.stage = 7
        $ teacher.breast_weight = 1.1
        $ teacher.breast_cup = "34D"
        $ teacher.breast_size = 38.2
        $ teacher.ass_size = 42.5
        $ teacher.waist_size = 32.8
        $ teacher.stomach_capacity = 2.3
        $ teacher.leanweight = 39.1
        return
    elif teacher.weight >= 68:
        $ teacher.stage = 6
        $ teacher.breast_weight = 1.05
        $ teacher.breast_cup = "34D"
        $ teacher.breast_size = 37.6
        $ teacher.ass_size = 41.2
        $ teacher.waist_size = 31.1
        $ teacher.stomach_capacity = 2.1
        $ teacher.leanweight = 39.3
        return
    elif teacher.weight >= 64:
        $ teacher.stage = 5
        $ teacher.breast_weight = 1
        $ teacher.breast_cup = "32E"
        $ teacher.breast_size = 37.1
        $ teacher.ass_size = 40.3
        $ teacher.waist_size = 29.6
        $ teacher.stomach_capacity = 2
        $ teacher.leanweight = 39.5
        return
    elif teacher.weight >= 61:
        $ teacher.stage = 4
        $ teacher.breast_weight = 0.95
        $ teacher.breast_cup = "32E"
        $ teacher.breast_size = 37.0
        $ teacher.ass_size = 39.9
        $ teacher.waist_size = 28.0
        $ teacher.stomach_capacity = 1.9
        $ teacher.leanweight = 39.6
        return
    elif teacher.weight >= 58:
        $ teacher.stage = 3
        $ teacher.breast_weight = 0.9
        $ teacher.breast_cup = "32E"
        $ teacher.breast_size = 36.5
        $ teacher.ass_size = 39.0
        $ teacher.waist_size = 26.3
        $ teacher.stomach_capacity = 1.8
        $ teacher.leanweight = 39.7
        return
    elif teacher.weight >= 55:
        $ teacher.stage = 2
        $ teacher.breast_weight = 0.85
        $ teacher.breast_cup = "32D"
        $ teacher.breast_size = 36.4
        $ teacher.ass_size = 37.4
        $ teacher.waist_size = 24.6
        $ teacher.stomach_capacity = 1.7
        $ teacher.leanweight = 39.9
        return
    else:
        $ teacher.stage = 1
        return
