label teaching_calories1:
    call rngteachingscene from _call_rngteachingscene
    teacher "Today I want to teach you about the basics of calories."
    teacher "Calories are a unit of energy we often use for measuring the energy intake and output of our bodies."
    call rngteachingscene from _call_rngteachingscene_1
    teacher "In most cases whenever someone says calories they actually mean Kilocalories, which is one thousand calories."
    teacher "This is shortened to Kcal on food and drink packages."
    call rngteachingscene from _call_rngteachingscene_2
    teacher "Because all units of energy are interchangeable, we can convert Kcal to Joules or Watts."
    teacher "All food and drinks are required to state the amount of Kcal contained inside."
    call rngteachingscene from _call_rngteachingscene_3
    teacher "We'll go into more detail about the effects excess calories can have on our weight in a future lesson."
    $ teaching_calories_times = 1
    return

label teaching_calories2:
    call rngteachingscene from _call_rngteachingscene_4
    teacher "So, let's continue with calories."
    teacher "Our bodies use energy every day. The amount we use depends on our weight, height, and how active we are."
    teacher "For example, my body and lifestyle require around 2200Kcal a day."
    call rngteachingscene from _call_rngteachingscene_5
    teacher "If I were to exceed this amount, the excess energy would be stored as fat."
    teacher "If I happen to consume less than 2200Kcal a day, then my body would turn the stored fat back into energy."
    teacher "So in short, bodyfat acts like some sort of battery for the energy your body uses to function."
    call rngteachingscene from _call_rngteachingscene_6
    if persistent.imperial:
        teacher "For the human body to gain 2.2lbs of fat it needs around 7700Kcal of excess energy."
    else:
        teacher "For the human body to gain 1Kg of fat it needs around 7700Kcal of excess energy."
    teacher "That’s all for now about calories but keep them in mind. They will be very important throughout the course of our lessons."
    $ teaching_calories_check = 1
    return

label teaching_terminology1:
    call rngteachingscene from _call_rngteachingscene_7
    teacher "Let’s talk about some weight gain related terminology."
    teacher "If you look online there are loads of words and abbreviations that are used."
    teacher "I will explain what some of them mean."
    call rngteachingscene from _call_rngteachingscene_8
    teacher "Let's start with feedee."
    teacher "A feedee is someone who enjoys being fed and sexually enjoys getting fatter. A feedee is often accompanied by a feeder."
    call rngteachingscene from _call_rngteachingscene_9
    teacher "A feeder is a person that gets enjoyment out of feeding others and watching them become fatter. In most cases the feeder has no interest in gaining weight themselves."
    teacher "There is an important distinction for a feeder; the feeder not only encourages the other person to gain weight but also provides the food."
    call rngteachingscene from _call_rngteachingscene_10
    teacher "A person that enjoys encouraging and watching others become fatter, without providing food or money for food, is called an encourager."
    teacher "Then there is also the gainer. A gainer is - just like the feedee - interested in gaining weight themselves."
    call rngteachingscene from _call_rngteachingscene_11
    teacher "But an important distinction is the fact that a gainer does all the feeding and gaining themselves, there is no feeder involved."
    teacher "There are mutual gainers. These are multiple people that love to fatten up together - encouraging each other along the way."
    call rngteachingscene from _call_rngteachingscene_12
    teacher "A foodee is someone who loves eating a lot of food, but has no interest in actively gaining weight."
    teacher "And the last term we will discuss today is the fat admirer, often called FA or chubby chaser."
    call rngteachingscene from _call_rngteachingscene_13
    teacher "This is a person who is sexually attracted to larger people, without any of the stuff we talked about before."
    teacher "We will continue discussing terminology next time."
    $ teaching_terminology_times = 1
    return

label teaching_terminology2:
    call rngteachingscene from _call_rngteachingscene_14
    teacher "So, last time we discussed some terms used to identify people's intentions in relation to gaining weight."
    teacher "Today I want to address some of the terms used to identify how big a person is."
    call rngteachingscene from _call_rngteachingscene_15
    teacher "Common terms like thin, thick and chubby are used for people with smaller size bodies."
    teacher "But larger people get categorized by terms like BBW, SSBBW and USSBBW."
    call rngteachingscene from _call_rngteachingscene_16
    teacher "BBW is an abbreviation for Big Beautiful Woman, ladies in this category generally weigh between 200 lbs (91 kg) and 350 lbs (159kg)"
    teacher "The exact weight can be different depending on height."
    call rngteachingscene from _call_rngteachingscene_17
    teacher "SSBBW is an abbreviation for Super Sized Big Beautiful Woman. Ladies in this category generally weigh between 350 lbs (159 kg) and 600 lbs (272 kg)."
    teacher "Humans most often aren't really able to gain more than the max weight of an SSBBW."
    call rngteachingscene from _call_rngteachingscene_18
    teacher "A SSBBW close to the max weight is a gigantic woman, and is immediately noticed in public."
    teacher "USSBBW is an abbreviation for Ultra Super Sized Big Beautiful Woman. Ladies in this category generally weigh more than 600 lbs (272 kg)."
    call rngteachingscene from _call_rngteachingscene_19
    teacher "Some people in the USSBBW class become immobile."
    teacher "This concludes all the terminology teaching."
    $ teaching_terminology_check = 1
    return

label corndog_unlock:
    call rngteachingscene from _call_rngteachingscene_20
    teacher "The corndog?"
    teacher "I love corndogs. Thankfully I can get one from the dining hall. Be right back."
    "After about five minutes, Daisy comes back with a corndog."
    image uni_sexy_teacher_food_eating_corndog = "/teacher/[teacher.stage]/4/food_eating_corndog.webp"
    scene uni_sexy_teacher_food_eating_corndog
    teacher "Mmm, this is really good."
    "Daisy eats the corndog in record time."
    call rngteachingscene from _call_rngteachingscene_21
    teacher "So, let me explain what a corndog is and if it can help me gain weight."
    teacher "A corndog is classified as fast food."
    call rngteachingscene from _call_rngteachingscene_22
    teacher "You take a sausage (usually a hot dog), put it on a stick, coat it in a thick layer of cornmeal batter and then deep fry it."
    teacher "The result will be a corndog."
    call rngteachingscene from _call_rngteachingscene_23
    teacher "An average corndog contains between 400 and 500 Kcal."
    teacher "Not only does it contain a lot of calories, it also contains a lot of fat."
    call rngteachingscene from _call_rngteachingscene_24
    teacher "This is because it’s a deep fried dish."
    teacher "So yeah, eating a lot of corndogs will make you gain weight."
    $ corndogunlock = 1
    $ teaching_corndog_check = 1
    "You unlocked the Corndog!"
    return

label milkshake_unlock:
    call rngteachingscene from _call_rngteachingscene_25
    teacher "You want to learn about milkshakes?"
    teacher "Well, you got the right person for that."
    call rngteachingscene from _call_rngteachingscene_26
    teacher "My love for milkshake is even bigger than the amount of food my stomach can hold."
    teacher "So creamy, sweet and cold."
    teacher "I’m going to go get a milkshake right away."
    "Daisy runs off to get a milkshake."
    image uni_sexy_teacher_food_eating_milkshake = "/teacher/[teacher.stage]/4/food_eating_milkshake.webp"
    scene uni_sexy_teacher_food_eating_milkshake
    "Seven minutes later."
    teacher "I got my milkshake."
    fs "And now she no longer has a milkshake."
    call rngteachingscene from _call_rngteachingscene_27
    teacher "That was great. It’s been way too long since I last had one of those."
    teacher "So let's talk about what a milkshake is and its nutritional values."
    call rngteachingscene from _call_rngteachingscene_28
    teacher "A milkshake is a sweet beverage made by blending milk, ice cream and a flavor, for example strawberry."
    teacher "A big milkshake contains more than 400 calories."
    call rngteachingscene from _call_rngteachingscene_29
    teacher "But the biggest fattener inside a milkshake is the sugar."
    teacher "One big milkshake contains about seventy-five grams of sugar."
    call rngteachingscene from _call_rngteachingscene_30
    teacher "That’s the equivalent of about nineteen sugar cubes."
    teacher "To conclude our lesson, drinking milkshakes will indeed make you gain lots of weight."
    $ milkshakeunlock = 1
    $ teaching_milkshake_check = 1
    "You unlocked the Milkshake!"
    return

label onionring_unlock:
    call rngteachingscene from _call_rngteachingscene_31
    teacher "Ohhh, onion rings!"
    teacher "Believe me when I say that I’ve eaten more than my fair share of onion rings."
    call rngteachingscene from _call_rngteachingscene_32
    teacher "So I believe I’m more than qualified to talk about them."
    teacher "Before that, let me go grab some."
    "Daisy leaves for a while."
    image uni_sexy_teacher_food_eating_onionrings = "/teacher/[teacher.stage]/4/food_eating_onionrings.webp"
    scene uni_sexy_teacher_food_eating_onionrings
    teacher "I got some delicious onion rings."
    teacher "They taste great, like always."
    call rngteachingscene from _call_rngteachingscene_33
    teacher "Onion rings are made by chopping onions in thin rings, putting those in batter and then deep frying them."
    teacher "One serving of standard, fast food onion rings contains about 450 calories."
    call rngteachingscene from _call_rngteachingscene_34
    teacher "Because they are deep fried, they contain a large amount of fat."
    teacher "We can conclude that onion rings are quite fattening, especially if you eat them with sauce."
    $ onionringunlock = 1
    $ teaching_onionring_check = 1
    "You unlocked Onion rings!"
    return

label bbq_unlock:
    #Image: Daisy standing next to the desk with the boxes balanced on top.
    "Placing the boxes on top of the desk, she turns back to face the class."
    teacher "Today I’ll be teaching you all about the wonderful world of barbequed food."
    #Image: Daisy holding up a barbequed chicken leg.
    "Opening up the top box, Daisy pulls out a chicken leg dripping with barbeque sauce."
    teacher "Now the term barbeque is said to be created from a Caribbean tribe called the Taino. The word is taken from the expression barbacoa, which referred to grilling on a raised wooden grate."
    #Image: Daisy eating the chicken leg
    "Taking a momentary pause, Daisy stops to strip the chicken leg down to the bone with her teeth. Tossing the remains of her snack into a trash can, she moves on to another box."
    #Image: Daisy holding up a rack of barbequed ribs.
    "Opening up another box, she pulls out a rack of ribs that makes several students in the class lick their lips from its sight and smell."
    teacher "However, the world of barbeque has expanded far beyond the original definition. The term now refers to a wide variety of different food and techniques."
    teacher "Everything from the humble backyard grilling of hotdogs to the painstaking process of cooking pork over long hours."
    teacher "Though they all can share the same term, each and every dish has their own qualities to make them stand out. Mainly, how great they taste."
    #Image: Daisy eating the rack of ribs.
    "Finished with her lecture, Daisy proceeds to tear the meat from the bones. Managing to finish it all off in no time at all, she wipes her fingers clean before approaching the boxes once more."
    #Image: Daisy eating different kinds of barbequed food.
    "Moving like she’s been possessed, Daisy proceeds to tear through her collection of barbeque."
    "The other students and I can only watch as she makes a complete pig of herself. She manages to just barely empty out all the boxes by the time class ends."
    #Image: Daisy slumped in her chair, rubbing her stomach.
    teacher "Whoops, lost track of time there. That’ll be all for today. Oh, and feel free to bring me more barbeque if you’d like. Needless to say, I’ve become quite the fan."
    "Barbeque has been unlocked."
    $ bbqunlock = 1
    $ teaching_bbq_check = 1
    return

label hedonism_through_the_ages1:
    #Part 1: Ancient Greece
    call rngteachingscene from _call_rngteachingscene_35
    teacher "Today, I would like to talk to you all about the origin of the word, hedonism since it goes hand in hand with gaining weight."
    teacher "The word itself is derived from the Greek goddess, Hedone whose name translates to pleasure."
    teacher "I can tell by the look on your faces that you’ve never heard of her before."
    call rngteachingscene from _call_rngteachingscene_71
    teacher "That’s probably because the main Greek deity you think of when it comes to indulgence is none other than Dionysus."
    teacher "This is probably due to the fact that he’s most known for his proclivity towards non-stop partying and drinking."
    teacher "It’s no wonder why the Greeks took to his worship so easily considering their own desire for indulgence."
    call rngteachingscene from _call_rngteachingscene_72
    teacher "Fittingly, his followers were eager to spread his teachings through dancing, drink, and indulgence. And of course, they were always looking to recruit people to join in their parties."
    teacher "While some refused, there was a warning for those who tried to stop the followers’ festivities."
    teacher "Those who don’t give themselves to the little madness may fall victim to the great madness."
    call rngteachingscene from _call_rngteachingscene_73
    teacher "In short, they were trying to get people to indulge every now and then to avoid becoming overwhelmed by their pent up desires."
    teacher "Looking at other parts of Greek society, we have to assume that the worst case scenario was a rare occurrence."
    teacher "However, they weren’t the only ones over the course of human history that valued copious food and drink. However, that’s all the time we have for today."
    $ teaching_hedonism_times = 1
    return

label hedonism_through_the_ages2:
    #Part 2: Middle Ages
    call rngteachingscene from _call_rngteachingscene_74
    teacher "Last time we broached the topic of what hedonism meant to ancient Greeks."
    teacher "While I could spend the entire semester talking about how they indulged themselves."
    teacher "I believe it would be better for us to summarize another part of history notable for indulgence: The Middle Ages."
    call rngteachingscene from _call_rngteachingscene_75
    teacher "This period in time is a little surprising when it comes to thinking about it in terms of indulgence."
    teacher "After all, most people were left to live in single room huts while tilling the farms for their lords. It doesn’t exactly provide the opportunity to stuff their faces at will."
    teacher "However, there was a small group of people that had more than enough wealth to fatten themselves to their heart’s content."
    call rngteachingscene from _call_rngteachingscene_76
    teacher "It was a common practice for royalty back in those times to flaunt their wealth by purposefully making themselves as fat as possible."
    teacher "You weren’t considered a proper noble unless you were at least twice the size of a normal person."
    teacher "Various parties and feasts were held to maintain this status quo."
    call rngteachingscene from _call_rngteachingscene_77
    teacher "While these did wonders for making the wealthy elite grow close to one another, they unfortunately didn’t share their generosity with the rest of the populace."
    teacher "As for the dire consequences of these actions…well, there’s a reason “Let them eat cake” is such an infamous quote."
    call rngteachingscene from _call_rngteachingscene_78
    teacher "While indulgent feasting has become more accessible since those days, a lot has changed. Such as our-"
    "Daisy is cut short by the ring of the bell."
    call rngteachingscene from _call_rngteachingscene_79
    teacher "Ah I guess that’s all for today. We’ll have to continue this at another time."
    $ teaching_hedonism_times = 2
    return

label hedonism_through_the_ages3:
    #Part 3: Modern Age
    call rngteachingscene from _call_rngteachingscene_80
    teacher "Catching up with where we were last time, our modern times have developed into a society that still clings to the old monarchies’ idealization of indulgence."
    teacher "The main difference is how much work has been done to give everyone a chance to be a hedonist."
    call rngteachingscene from _call_rngteachingscene_81
    teacher "Everything from our access to cheap, fattening food to various ways to meet with others for…carnal desires has been made much easier due to modern technology."
    teacher "To this day, society still embodies the desire to seek pleasure that was seen with the followers of Dionysus and royalty."
    call rngteachingscene from _call_rngteachingscene_82
    teacher "Whether that’s buffet halls or night clubs, we all have our own dens of hedonism."
    teacher "Then again, this is all just part of a much larger movement of our modern age idealizing consuming to our heart’s content."
    teacher "But that is a lesson for another day. That will be all for now."
    $ teaching_hedonism_check = 1
    return

label food_addiction1:
    #Part 1: Food Addiction Introduction
    call rngteachingscene from _call_rngteachingscene_83
    teacher "While we like to talk about the positive side of engorging one self, it would be irresponsible for me not to discuss one of the unsavory sides of it."
    teacher "As much as I hate to admit it, there is such a thing as having too much of a good thing. In this case, I’m talking specifically about food addiction."
    call rngteachingscene from _call_rngteachingscene_84
    teacher "Just like a drug, some people turn to food to deal with stress and a lack of dopamine. While this is all fine and good in small doses, the negative effects go far beyond gaining weight."
    teacher "Poor health, neglecting basic care, and going into debt for the sake of extravagant feasts are just some of the consequences of unwise binging."
    call rngteachingscene from _call_rngteachingscene_85
    teacher "Sorry to leave things today on a depressing note, but I think that’s all we have time for right now. I promise I’ll try to make the next lesson more uplifting."
    $ teaching_addiction_times = 1
    return

label food_addiction2:
    #Part 2: Food Addiction Treatment
    call rngteachingscene from _call_rngteachingscene_86
    teacher "Last time we broached the topic of food addiction."
    teacher "While it a very serious issue that could afflict anyone with an inability to control themselves, there are ways to treat it or at the very least make it more manageable."
    call rngteachingscene from _call_rngteachingscene_87
    teacher "To start, it’s important to identify what are your danger foods so to speak and to take steps to avoid them."
    teacher "If you can properly recognize what’s causing these unhealthy habits, it should help in letting you return to a regular diet."
    teacher "There’s also a matter of purposefully preventing situations that could trigger these bouts of bad binging."
    call rngteachingscene from _call_rngteachingscene_88
    teacher "Pre-planning healthy meals to avoid being forced to come up with something on the spot is one such method."
    teacher "If you’re unable to commit to treatment by yourself, various hotlines and treatment centers are available."
    teacher "I’ll be handing out a page of information with these websites and phone numbers after class."
    call rngteachingscene from _call_rngteachingscene_89
    teacher "Even the helping hand of your friends and loved ones are crucial to supporting your path back to a positive relationship with food."
    teacher "More than likely, they’re just as eager as you are to get you back to a healthy state."
    call rngteachingscene from _call_rngteachingscene_90
    teacher "While I prefer the foodie lifestyle myself, I will recognize that you need to be able to know when to stop."
    teacher "If stuffing yourself silly is making things unpleasant for both you and those around you, then I don’t want you to force yourselves."
    call rngteachingscene from _call_rngteachingscene_91
    teacher "That being said, I would like to take this opportunity to let you all know that I have a very healthy relationship with my own binging."
    teacher "In-between these massive stuffing sessions, I make sure to take a breather and assess where I need to adjust my diet to avoid going too far off the deep end."
    teacher "If nothing else, I ask that you all keep in mind to know when to stop indulging yourselves when it begins to have major, negative effects on your lives."
    $ teaching_addiction_check = 1
    return

label food_industry1:
    #Part 1: Fast Food
    call rngteachingscene from _call_rngteachingscene_92
    teacher "Today I would like to broach the topic of the corporate side of food. Specifically the various factors their business contributes to how we consume things."
    teacher "Now, one of the most innovative inventions of the 20th century, in my opinion at least, is the concept of fast food."
    call rngteachingscene from _call_rngteachingscene_93
    teacher "Made for hungry people without time to sit down for a proper meal, these quick service restaurants have become a staple of modern life."
    teacher "The tradeoff for the sped up creation process was that the employees didn’t have the opportunity to carefully craft the meals."
    teacher "Not to mention the need for said food to be easily transported after being picked up."
    call rngteachingscene from _call_rngteachingscene_94
    teacher "Because of these factors and more, the eateries turned towards various food additives and unhealthy preparation techniques."
    teacher "While this did wonders for the taste and cost, it was in exchange for diminishing dietary values."
    call rngteachingscene from _call_rngteachingscene_95
    teacher "Of course, this has led to many fast food eateries being associated with obesity and unhealthy lifestyles."
    teacher "There was even an infamous documentary that tried to show off the dark side of these type of establishments."
    call rngteachingscene from _call_rngteachingscene_96
    teacher "However, it is important to note that everything, including healthy food, is bad in extreme portions."
    teacher "As long as you don’t eat this kind of cuisine for every meal for every day, you should be able to properly enjoy it from time to time."
    teacher "Well, as long as the portions sizes remain at a moderate size."
    $ teaching_industry_times = 1
    return

label food_industry2:
    #Part 2: Larger Portion Sizes
    call rngteachingscene from _call_rngteachingscene_97
    teacher "Last we left off on the subject of food corporations, I briefly touched on the topic of portion sizes."
    teacher "You’ve probably noticed the labels they place on food packaging. This information is supposed to help consumers understand what makes up what they’re eating."
    call rngteachingscene from _call_rngteachingscene_98
    teacher "Things like calories, sugar, sodium levels, and ingredients, to name a few."
    teacher "However, what most consumers miss is probably the most important detail: portion size."
    call rngteachingscene from _call_rngteachingscene_99
    teacher "What each label is talking about specifically is the amount you’re supposed to consume when you eat the recommended amount."
    teacher "A lot of people make the mistake of underestimating the nutritional impact because they fail to read this piece of information. However, that’s not entirely their fault."
    call rngteachingscene from _call_rngteachingscene_100
    teacher "Every so often, the people in charge of these labels decide to use it to their advantage by tweaking the portion sizes."
    teacher "Shrinking the amount listed on the packaging can lead people to misread what’s inside of their food."
    teacher "While this has the expected effect of making people overindulge themselves, its main purpose is to get people to eat their products faster."
    call rngteachingscene from _call_rngteachingscene_101
    teacher "The quicker you work through a delicious box of snacks, the more likely you are to go back for more."
    teacher "This is far from the only body side effects created as a byproduct of greed, but that’s all we have time for today."
    $ teaching_industry_times = 2
    return

label food_industry3:
    #Part 3: Food Supplements
    call rngteachingscene from _call_rngteachingscene_102
    teacher "If you’ve been paying attention to our previous lessons, then you recall two important things."
    teacher "One, that fast food required unhealthy additives to keep their products tasty. And two, that corporations are always looking for ways to increase profits in any way possible."
    call rngteachingscene from _call_rngteachingscene_103
    teacher "These factors fueled the development of various additives that aim to please both needs."
    teacher "Think of things like preservatives, sodium, and plain old sugar. Each of these are squeezed into foods like frozen dinners and even juice to increase their shelf life and taste."
    call rngteachingscene from _call_rngteachingscene_104
    teacher "As we discussed earlier, this is all in the service of maximizing profits while keeping costs low."
    teacher "Because of this, corporations tend to overlook the negative side effects of these various additives."
    teacher "Like, grossly inflating calorie count and destroying a person’s diet."
    call rngteachingscene from _call_rngteachingscene_105
    teacher "However, this isn’t all doom and gloom. As long as you make sure to read before you eat, you can properly use these additives to your advantage."
    teacher "Whether that’s stocking up with food that will last you for a while or purposefully indulging in fatty meals to increase your weight, you can work alongside their greed to meet your own goals."
    call rngteachingscene from _call_rngteachingscene_106
    teacher "It’s all a matter of out thinking them while keeping yourself in control."
    teacher "Failing that, I would happy just knowing that you all learned to be more observant of what you put into your bodies after this class is done."
    $ teaching_industry_check = 1
    return

label animal_kingdom1:
    #Part 1: Animal Blubber
    call rngteachingscene from _call_rngteachingscene_107
    teacher "I am aware that this class is mainly focused on the nutritional studies of humans. That being said, we can look at other creatures to get a better understanding the benefits of fat."
    teacher "Let’s start with a term that is sometimes used interchangeably with fat: Blubber."
    call rngteachingscene from _call_rngteachingscene_108
    teacher "While this can be used as a derogatory term for overweight people, for certain animals, blubber is crucial to surviving and thriving in colder climates."
    teacher "Creatures like seals and whales put this extra padding to good use in arctic, marine habitats. It’s like a thick coat to keep themselves warm in temperatures far below zero."
    call rngteachingscene from _call_rngteachingscene_109
    teacher "While humans have turned towards a more advanced solution in the form of warm clothes, I’m a bit curious whether or not someone with a blubbery body could do well in the cold."
    teacher "However, I believe that’s a theory best left as a fun thought experiment. I don’t intend to make any trips to the arctic anytime soon."
    $ teaching_animal_times = 1
    return

label animal_kingdom2:
    #Part 2: Hibernation
    call rngteachingscene from _call_rngteachingscene_110
    teacher "For those of you who are unaware or can’t remember, fat cells are used to store excess calories for the body."
    teacher "This feature is particularly important for today’s topic: hibernation."
    teacher "While we recently talked about how blubber is a way to combat colder climates, it’s not the only natural solution."
    call rngteachingscene from _call_rngteachingscene_111
    teacher "Rather than have to endure the harsh conditions, certain animals decide to skip it entirely with a nice, long nap."
    teacher "Hibernation is crucial for certain species when it comes to surviving the winter. However, it’s not as simple as merely finding a soft pile of leaves and closing their eyes."
    call rngteachingscene from _call_rngteachingscene_112
    teacher "Take for example a bear. Before they go into their long hibernation, they work hard to gather as much food as possible."
    teacher "Their nature as omnivores means that they eat anything they can get their paws on. Anything from berries, to salmon, to whatever they can “borrow” from an unattended picnic basket."
    call rngteachingscene from _call_rngteachingscene_113
    teacher "They do the equivalent of binging at an all you can eat buffet. Once they’ve properly built up enough bulk, they end up sleeping it off over the course of their hibernation."
    teacher "I’m sure you can all relate to wanting to pass out after eating a big meal. Unfortunately, or fortunately in my case, losing weight isn’t as easy as just sleeping it off for humans."
    call rngteachingscene from _call_rngteachingscene_114
    teacher "That all being said, bears don’t lose every bit of their fat. After all, they still need it to be apex predators of their environment. Like certain other animals, such as…"
    teacher "Ah, I’m afraid I that I might have gone on a little too long. We’ll have to cut things off for today."
    $ teaching_animal_times = 2
    return

label animal_kingdom3:
    #Part 3: Large Savannah Animals
    call rngteachingscene from _call_rngteachingscene_115
    teacher "Last we left off on our animal kingdom discussion, we were talking about the fearsome bear."
    teacher "While it’s a top predator for a variety of reasons, one of the major ones is their bulk."
    teacher "This rule of a large size equals large power is true for multiple animals."
    call rngteachingscene from _call_rngteachingscene_116
    teacher "Such as the whales we mentioned before and even in the distant past with dinosaurs such as a Brontosaurus or the fearsome T-Rex."
    teacher "However, I believe that the best place to look for examples of size equaling dominance is in the African Savannah."
    call rngteachingscene from _call_rngteachingscene_117
    teacher "This habitat is dominated by large beasts. I’m specifically talking about creatures such as hippopotamuses, rhinoceroses, and elephants."
    teacher "These massive animals are the dominant creatures of their domains. Even vicious predators like lions, cheetahs, and hyenas have to pay them respect when going on hunts."
    call rngteachingscene from _call_rngteachingscene_118
    teacher "Whether it’s a rhino using its bulk to put some power behind its horn or the elephant effortlessly trampling things smaller than it, their feats are only made possible thanks to their size."
    teacher "As for hippos…well, there’s only so much I can talk about in a class setting and keep things polite."
    call rngteachingscene from _call_rngteachingscene_119
    teacher "What I can tell you is that these creatures kill more people every year than even the infamous crocodile."
    teacher "These animals show the true extent of how fat can help them survive in nature."
    teacher "However, there is an entirely different group of animals that survive and thrive in our own society because of their fat."
    $ teaching_animal_times = 3
    return

label animal_kingdom4:
    #Part 4: Farm Animals
    call rngteachingscene from _call_rngteachingscene_120
    teacher "Today I would like to finish up our animal discussion by diving into the topic of how their fat can help us directly. Specifically, when it comes to putting food on our tables."
    teacher "For the longest time, humans have taken to domesticating different types of animals for the sake of their own benefit."
    call rngteachingscene from _call_rngteachingscene_121
    teacher "Everything from sheep, to cows, to chickens, were put under our care in exchange for their goods."
    teacher "Because of this, we have seen a drastic increase in their populations to go along with our own civilization’s growth."
    teacher "However, a herd of 100 pigs isn’t worth much if they don’t have any meat on their bones."
    call rngteachingscene from _call_rngteachingscene_122
    teacher "The trick to producing quality food products is to ensure that the animals are kept happy and healthy over their lifetime."
    teacher "That means giving them proper diets and living conditions to shape their bodies into our desired form."
    call rngteachingscene from _call_rngteachingscene_123
    teacher "Now granted, there have been cases of less ethical practices done on farms to reach the required results for the animals with no concern for their well-being."
    teacher "Things such as chickens kept in cages for all of their lives or feeding supplements to pigs to make them grow."
    call rngteachingscene from _call_rngteachingscene_124
    teacher "For cows, there have been cases where they have been force fed in fattening pens where they’re not even allowed to move."
    teacher "They spend every day of their lives stuck in these cages, with nothing to do but eat and grow bigger."
    call rngteachingscene from _call_rngteachingscene_125
    teacher "I’ll admit, I wouldn’t mind trying out that kind of lifestyle, but it’s not exactly great for the animals."
    teacher "Even if their ultimate fate is to become food on our plate, we should make sure they’re taken proper care of. It makes sure the meals they produce are extra tasty."
    $ teaching_animal_check = 1
    return

label body_types1:
    #Part 1: Realistic Shapes
    call rngteachingscene from _call_rngteachingscene_126
    teacher "When it comes to describing body types, there are certain terms that act as a way to quickly get across the general idea of what a person looks like."
    teacher "For now, I would like to focus on a small number of commonly accepted terms."
    call rngteachingscene from _call_rngteachingscene_127
    teacher "One that you see come up mostly in the modeling world is the hourglass shape. This type of figure was very popular in the 1950s, heralded as the ideal type a woman should strive for."
    teacher "That being said, an hourglass figure isn't exclusive to skinny people. There are many that have their mass distributed towards their chests and backsides when they put on weight."
    call rngteachingscene from _call_rngteachingscene_128
    teacher "On the opposite side of the spectrum, we have figures that resemble an apple. This shape generally has the weight centered around the belly to create a rounded appearance."
    teacher "In the same vein of fruit-based figures we have the pear. This one has the person's weight mainly distributed towards their hips and backsides."
    call rngteachingscene from _call_rngteachingscene_129
    teacher "A mutation of this shape is known as a bell, typically created from the person resembling, well, a bell."
    teacher "In truth, there are countless other shapes a person's body can take when gaining weight. It's just another way that we diversify the lovely forms that fat can create."
    $ teaching_bodytypes_times = 1
    return

label body_types2:
    #Part 2: Fantasy Body Types
    call rngteachingscene from _call_rngteachingscene_130
    teacher "Following a previous discussion about different figures created by weight gain, a few students came to me to ask some questions."
    teacher "Some of them brought to my attention some more…outlandish shapes that are prevalent in the community’s minds."
    call rngteachingscene from _call_rngteachingscene_131
    teacher "Sorry to disappoint you all, but when I said that people can take on numerous forms, I failed to mention that there are certain limitations."
    teacher "Things such as having to adhere to the laws of reality."
    call rngteachingscene from _call_rngteachingscene_132
    teacher "While I would like to push the issue aside all together, I would be a failure of a teacher if I didn’t at least acknowledge some of these fantasy shapes that come up in conversations about big bodies."
    teacher "The first is a shape that resembles reality but goes far beyond human limitations. That of what some refer to as a blob."
    call rngteachingscene from _call_rngteachingscene_133
    teacher "Blobs are pretty much what you expect. Massive piles of flesh that take up enormous amounts of space."
    teacher "Think of it as an all-encompassing organism capable of sucking up everything in its path. In fact, the name comes from a pretty famous monster from an old film."
    call rngteachingscene from _call_rngteachingscene_134
    teacher "Even ignoring the horror-movie like aspects associated with the form, it’s still out of human reach. A person’s body can only grow so big before physical limitations take their toll."
    teacher "Going even further in terms of what human bodies are capable of is the sphere shape. Something that comes up quite a lot when speaking of fetishes adjacent to weight gain."
    call rngteachingscene from _call_rngteachingscene_135
    teacher "The sphere shape is typically shown as a person’s becoming a literal orb. Basically overshadowing most, if not all, other parts of the body."
    teacher "No fat rolls, breasts, butt, or sometimes even limbs to ruin the figure. It all becomes sunken into this form."
    teacher "As ridiculous as this figure is, the reason it keeps coming up is because it shows up in a variety of different fetishes."
    call rngteachingscene from _call_rngteachingscene_136
    teacher "Want just a sloshy, round orb? Water expansion. Want to imitate a balloon and fly around? Inflation. Would you like to win first prize at a fair? Blueberry or similarly rounded fruit expansion."
    teacher "I have to admit that I’ve looked into these kinds of things myself out of curiosity. While they do offer a nice fantasy, I regretfully have to accept that they’re not an achievable goal."
    call rngteachingscene from _call_rngteachingscene_137
    teacher "That being said, the fact that they’re so common in the fetish community means-"
    teacher "that there are plenty of talented artists, animators, and writers who are more than willing to create pieces to simulate the experience."
    teacher "Now, what does this all have to do with a Nutritional Studies class? Admittedly, not much."
    call rngteachingscene from _call_rngteachingscene_138
    teacher "Let’s call this a little supplementary lesson on the nature of the kink community. You never know what kind of information will come in handy."
    $ teaching_bodytypes_check = 1
    return

label nature_nurture1:
    #Part 1: Nature vs Nurture Debate
    call rngteachingscene from _call_rngteachingscene_139
    teacher "Enlarging the scope of our studies a bit, today I would like to discuss what makes a person who they are. In particular, what factors have a greater influence on a body’s development."
    teacher "There has been a constant debate on what is the main contributor of this process. For some it’s a matter of who you are at birth."
    call rngteachingscene from _call_rngteachingscene_140
    teacher "For others, it’s more of where you are at birth and what happens to you afterwards in that environment."
    teacher "To put it simply, the debate is whether or not who we are is dependent on our inherent nature or how we were nurtured over the course of our upbringing."
    teacher "The reason this has gone on for so long is because it’s not an easy question to answer."
    call rngteachingscene from _call_rngteachingscene_141
    teacher "Since human beings do not have the ability to peek into alternate realities, we can’t tell if a person would turn out differently if they were raised in a different environment."
    teacher "Any data we’ve been able to gather has come from unfortunate events. Think of circumstances such as identical twins being separated at birth."
    call rngteachingscene from _call_rngteachingscene_142
    teacher "While scientists are eager to get the data, the question then becomes if it is ethical to use the data from such a study."
    teacher "After hearing all of that, you’re probably wondering what this has to do with our class."
    call rngteachingscene from _call_rngteachingscene_143
    teacher "Well, I figured I would go over the general idea of this debate before we go over the various genetic and environmental factors that can have an effect on a person’s weight."
    teacher "However, that will have to wait for next time. We’ll hit the ground running with a focus on nature when we return."
    $ teaching_naturenurture_times = 1
    return

label nature_nurture2:
    #Part 2: Nature
    call rngteachingscene from _call_rngteachingscene_144
    teacher "In terms of nature having effects on a person’s weight gain, the easiest place to start is to consider where they came from."
    teacher "What I’m talking about is looking towards their ancestors to see what possible genetics could determine a person’s figure."
    call rngteachingscene from _call_rngteachingscene_145
    teacher "Basically speaking, if your family is well known for being on the larger side, odds are that your genetics are pre-disposed to that kind of body type."
    teacher "This could also be a case of just being big boned or having a slow metabolism."
    teacher "Aside from just looking at your ancestors, the nature of who you are at birth is a major factor."
    call rngteachingscene from _call_rngteachingscene_146
    teacher "Things like personality, medical conditions, and preferences for different kinds of foods have a hand in deciding your ultimate fate."
    teacher "For example, if you have an overactive sweet tooth and a predisposition for experimentation, it could lead to a binge session of trying out the various pastries across many different bakeries."
    call rngteachingscene from _call_rngteachingscene_147
    teacher "The same could be said for if you wanted to take on a massive steak because that’s what your body deems appropriate to keep itself running."
    teacher "While we can’t decide the family we’re born in or what kind of genetics we have, it’s not the end all, be all for who we are. A lot of that can be sculpted by your own life choices."
    teacher "Then again, it could also be determined by what’s going on around you rather than inside of you."
    $ teaching_naturenurture_times = 2
    return

label nature_nurture3:
    #Part 3: Nurture
    call rngteachingscene from _call_rngteachingscene_148
    teacher "When it comes to how people choose to live their lives, there is indeed a perception that their choices are made by what they were brought up around."
    teacher "As I said before, you can’t decide who you’re born with, but you’re also incapable of choosing where you’re born."
    call rngteachingscene from _call_rngteachingscene_149
    teacher "Your environment has a larger impact on who you are as a person than you may imagine. A basic example is what kind of weather you prefer based on where you lived growing up."
    teacher "It’s the reason that some people can walk around in the snow wearing only shorts."
    call rngteachingscene from _call_rngteachingscene_150
    teacher "The same could be said for our eating habits. Say you were raised around a group of people that valued eating a lot of barbequed meat at every party."
    teacher "From there, you would probably work under the assumption that’s the tradition for most families."
    teacher "However, if you were raised entirely amongst vegans, your celebrations would most likely come along with sessions of stuffing your face with grilled veggies and fried tofu."
    call rngteachingscene from _call_rngteachingscene_151
    teacher "While these types of influences mixed with your genetics can have an impact on who you are and how your body develops, that’s not to say that they’re the end all, be all."
    teacher "Of course, your own personal choices have an effect."
    call rngteachingscene from _call_rngteachingscene_152
    teacher "Regardless of if you accept the factors of your environment and genetics or make the conscious choice to against them, at the end of the day it all depends on your own free will."
    teacher "Just be sure that you remain aware of the outside influences that could be affecting your decisions."
    $ teaching_naturenurture_check = 1
    return


label indulgence1:
    #Part 1: General Support
    call rngteachingscene from _call_rngteachingscene_153
    teacher "While you and your support circle can aid in your weight development, there is another, larger force that can assist you. Our own, modern society."
    teacher "It’s no secret that over the years our civilization has leaned towards helping us indulge ourselves."
    call rngteachingscene from _call_rngteachingscene_154
    teacher "Of course this isn’t true for every society based on their overall wealth, but for us, our overabundance of resources has given us plenty of opportunities to enjoy instances of extreme hedonism."
    teacher "Think back to what we discussed regarding how businesses manipulate their products to maximize profits. Supplements, easy access to food, etc."
    call rngteachingscene from _call_rngteachingscene_155
    teacher "Even if it’s not intentional, they’ve paved the way for feedees and feeders to thrive in this modern age."
    teacher "While we might have touched on a few of these methods, there are a few I wanted to elaborate on."
    call rngteachingscene from _call_rngteachingscene_156
    teacher "Specifically, how easy it is to gain weight and overeat without even thinking about it. We’ll go more in depth of what I mean next time."
    $ teaching_indulgence_times = 1
    return

label indulgence2:
    #Part 2: Delivery Service
    call rngteachingscene from _call_rngteachingscene_157
    teacher "I’m sure you’ve all felt this before. You come home from a long day, worn out by life’s many struggles."
    teacher "Maybe you did poorly on a test, your favorite dress got ripped, or an angry customer yelled at you during your work shift."
    call rngteachingscene from _call_rngteachingscene_158
    teacher "On these kinds of days, even the notion of having to cook for yourself seems like an insurmountable obstacle."
    teacher "Thankfully, the modern age has created a savior for your troubles. You get to have your own, warm meal without even having to leave the house."
    teacher "I’m talking about the various delivery services provided by the wonders of technology."
    call rngteachingscene from _call_rngteachingscene_159
    teacher "The first thing that comes to mind when talking about home delivered food is probably the classic pizza."
    teacher "While I’m a big fan of indulging in greasy, melty cheese, the options have expanded quite a bit over the years."
    call rngteachingscene from _call_rngteachingscene_160
    teacher "Thanks to various delivery services, practically anything you desire can be brought straight to your door."
    teacher "Anything from a bag of greasy burgers to a steak from a five star restaurant could be on your plate within an hour."
    call rngteachingscene from _call_rngteachingscene_161
    teacher "Regardless of where the food came from or how fancy it is, you’re given the chance to pig out on it in the comfort of your home, in only your underwear."
    teacher "I’ve used these services myself to great effect. Both for my own bad days and for days when I’m feeling extra…good."
    call rngteachingscene from _call_rngteachingscene_162
    teacher "I’d like to tell you more, but I believe that information is reserved for the privacy of myself and whoever I can tip well enough to keep a secret."
    $ teaching_indulgence_times = 2
    return

label indulgence3:
    #Part 3: Frozen Meals
    call rngteachingscene from _call_rngteachingscene_163
    teacher "Picture this. You’re going through the super market, trying to plan out what you’ll be eating for the upcoming week."
    teacher "Amidst the various ingredients and cooking appliances you’ll need, you have to carefully consider when you’ll actually have the time to put it all together."
    call rngteachingscene from _call_rngteachingscene_164
    teacher "That’s when you spot them as you wander down an aisle made up entirely of freezers."
    teacher "They offer you a solution to your problem. A fully prepared meal that requires a fraction of the time and effort to create it."
    teacher "A few of you have probably pieced together that I’m talking about frozen meals. A marvelous invention created back in the 1940s."
    call rngteachingscene from _call_rngteachingscene_165
    teacher "They were thought up as a way for people to enjoy restaurant quality food at their leisure. Just follow the instructions on the box and you’ll be treated to an easy, tasty meal."
    teacher "These became so popular, that a large number of people made them a staple of their evenings sitting in front of the television. This is how they came to be nicknamed TV Dinners."
    call rngteachingscene from _call_rngteachingscene_166
    teacher "The same wonders that have evolved delivery services have made their way into these frozen wonders."
    teacher "Providing a wide selection of different courses that can be ready to devour after a short stint in the microwave."
    call rngteachingscene from _call_rngteachingscene_167
    teacher "As wonderous as these are, I feel like it’s my duty to talk about their downsides."
    teacher "The quality of the taste varies since they have to make special accommodations for the food to be frozen in the first place."
    teacher "One of which are high levels of sodium that can cause havoc on your diet."
    call rngteachingscene from _call_rngteachingscene_168
    teacher "While I wouldn’t recommend eating them for every meal, they are quite a handy little gadget. Especially when they allow for the fast creation of feasts."
    teacher "I still remember the time I bought a five pound bag of chicken nuggets."
    teacher "Sure I nearly set my kitchen on fire from using the oven so much, but I’d say the indulgence was more than worth it."
    call rngteachingscene from _call_rngteachingscene_169
    teacher "To clarify, make sure you eat these things responsibly."
    teacher "I’d rather not have any of you miss class because your microwave blew up from trying to reheat a frozen burrito at four in the morning."
    $ teaching_indulgence_check = 1
    return

label fattening_careers1:
    #Part 1: Competitive Eating
    call rngteachingscene from _call_rngteachingscene_170
    teacher "We‘ve discussed in depth gaining weight for the purpose of leisure. This is my preferred use of it, however larger bodies open the doors for a multitude of different career paths."
    teacher "For instance, what if you could turn a massive appetite into a boon for a sport? A sport that has fierce competition, prizes as large as the athletes, and cheering crowds."
    call rngteachingscene from _call_rngteachingscene_171
    teacher "Competitive eating has gotten quite popular in recent years. With some even being broadcast on national television."
    teacher "Though it started off as a niche attraction found at only fairs or family gatherings, these tests of appetites have been steadily growing in appeal."
    teacher "This is due in part to it becoming more visible thanks to social media."
    call rngteachingscene from _call_rngteachingscene_172
    teacher "Not only does getting videos and images of people claiming victory over massive amounts of food gain interest from spectators, but they also garner attention for restaurants."
    teacher "Many eateries have gone out of their way to make special food challenges to draw in these titans of tummies to do fierce battle."
    call rngteachingscene from _call_rngteachingscene_173
    teacher "Usually with extravagant meals that could feed a family of four for a week."
    teacher "Whether it means trying to scarf down a massive platter of food within a time limit or going head to head with another big eater, each battle is as fierce as ever."
    teacher "I would highly recommend watching a few yourselves."
    call rngteachingscene from _call_rngteachingscene_174
    teacher "As for me, I prefer to keep my appetite reserved for friendly competition among friends. I may be a big eater, but I don’t think I could compare to the experts."
    teacher "That being said, if any of you want to try it for yourself, make sure you let me know. I’d be more than happy to root for you on the sidelines."
    $ teaching_careers_times = 1
    return

label fattening_careers2:
    #Part 2: Sumo Wrestling
    call rngteachingscene from _call_rngteachingscene_175
    teacher "There are many sports that favor those on the larger side. Things like weight lifting, American football, and hockey to name a few."
    teacher "However, one of the most prevalent, at least in one part of the world is the noble competition of sumo wrestling."
    teacher "It’s a classic fight where the goal is to use your bulk to push the opponent out of the fighting ring."
    call rngteachingscene from _call_rngteachingscene_176
    teacher "Sumo is a tradition that dates back to ancient times in Japan. It has dipped in and out popularity since then, but it still remains strong to this day."
    teacher "I can see the look in your eyes. You probably assume from pop culture that the sport is nothing more than fat men in diapers eating food and pushing each other around."
    call rngteachingscene from _call_rngteachingscene_177
    teacher "The truth is, sumo wrestlers have to go on a strict training regimen the same as any athlete."
    teacher "That means plenty of exercise to properly shape their fat and a specific diet to quickly pack on the pounds."
    teacher "During one of my trips to Japan, I got to sample a staple of sumo cuisine known as chankonabe. It’s a type of stew that’s packed full of different proteins to promote weight gain."
    call rngteachingscene from _call_rngteachingscene_178
    teacher "Back then, I was barely able to finish one bowl. Now, I think I might want to go toe to toe with one of the wrestlers thanks to all the stuffing you’ve helped me with during class."
    teacher "That being said, I’m in no rush to put on a mawashi myself and enter the ring. I’d rather leave that to the professionals."
    $ teaching_careers_times = 2
    return

label fattening_careers3:
    #Part 3: Plus-Sized Models
    call rngteachingscene from _call_rngteachingscene_179
    teacher "Finishing up our section of careers that larger bodies excel at, I would like to turn to one that’s not as obvious."
    teacher "You’ve probably seen a version of this when walking through a store and passed by a magazine rack."
    call rngteachingscene from _call_rngteachingscene_180
    teacher "A slender woman or fit guy with six-pack abs trying to sell you everything from perfumes to clothes, and even cars."
    teacher "While this was true for the longest time, in recent years the public’s reception has been to desire models that better represent the average person."
    call rngteachingscene from _call_rngteachingscene_181
    teacher "Ergo why there’s been a booming industry for photogenic people that are a little on the larger side."
    teacher "Plus-sized models are great for showcasing just how beautiful it can be to be big."
    teacher "Whether that’s with luscious love handles draped by skirts or a cute belly shown off by a two piece swimsuit that just barely covers up a set of buxom breasts."
    call rngteachingscene from _call_rngteachingscene_182
    teacher "For the more risqué, there’s also the nude shoots which show just how bold some of these models are about showing who they really are."
    teacher "It helps others who feel inadequate about their bodies get some self-confidence back."
    call rngteachingscene from _call_rngteachingscene_183
    teacher "Though we’ve gone over a plethora of different career paths, I think this is one of the few I’d actually like to try."
    teacher "Who knows, maybe you’ll see me on the cover of a magazine someday."
    $ teaching_careers_check = 1
    return

label feeder_feedee1:
    #Part 1: Consent
    call rngteachingscene from _call_rngteachingscene_184
    teacher "I’m assuming that at least one person here has gotten interested in trying out the feeder or feeder lifestyle."
    teacher "Even if no one wants to admit it out loud, I’d be more than a happy to give some guidelines."
    call rngteachingscene from _call_rngteachingscene_185
    teacher "The first lesson is also the most important one. We’re starting off with a concept that’s essential, not only for this, but for any kind of relationship: consent."
    teacher "The entire point of indulgence is to enjoy yourself. However, that shouldn’t be at the price of making someone else uncomfortable."
    call rngteachingscene from _call_rngteachingscene_186
    teacher "Before planning any feasts, trying out different fantasies, or even putting a single morsel of food into their mouth, you need to talk to your partner about it."
    teacher "Not only does this ensure they’re comfortable with the situation, but it also means making compromises that you can agree with."
    call rngteachingscene from _call_rngteachingscene_187
    teacher "Failing this crucial step can have dire consequences. Injuries, mental trauma, and abusive relationships just to name a few."
    teacher "Even if you don’t pursue being a feeder or feedee, please keep in mind that consent is paramount to any partnership."
    $ teaching_feederfeedee_times = 1
    return

label feeder_feedee2:
    #Part 2: Planning
    call rngteachingscene from _call_rngteachingscene_188
    teacher "When we last talked about consent, I mentioned speaking with your partners about what you want to do."
    teacher "Aside from making sure they’re comfortable with whatever ideas you have, this has the added benefit of being able to plan things out together."
    call rngteachingscene from _call_rngteachingscene_189
    teacher "Planning out your sessions is crucial to optimizing your enjoyment and avoiding disaster."
    teacher "Nothing can ruin the mood like being just about ready to start the feast only to realize you forgot to make a trip to the store."
    call rngteachingscene from _call_rngteachingscene_190
    teacher "Before initiating any feeding session, you need to sit down with your partner and figure out the how, where, and what of your plans."
    teacher "That means figuring out the exact steps required, a good location, any extra tools needed, and so on."
    teacher "For instance, say you want to pig out on a load of barbeque."
    call rngteachingscene from _call_rngteachingscene_191
    teacher "Aside from ordering the food, you want to make sure you have something nearby to keep things clean if you get too messy."
    teacher "Such as wipes or a tarp to avoid the sauce getting all over the floor."
    teacher "I will admit, failing this step in the process has led to some…less than savory memories."
    call rngteachingscene from _call_rngteachingscene_192
    teacher "I had to learn the hard way that just because a fast food place will give you a bulk order of burgers, doesn’t mean they will agree with your stomach."
    teacher "However, it’s because of that that I tend to always have a supply of antacids and other medicines nearby for any session."
    teacher "Even if you fail to plan, you can use that to your advantage when you make your next attempt."
    $ teaching_feederfeedee_times = 2
    return

label feeder_feedee3:
    #Part 3: Portions
    call rngteachingscene from _call_rngteachingscene_193
    teacher "So, after all you’ve seen and heard from me, you’re probably thinking about jumping right in to a feeding session."
    teacher "You’ve asked your partner for consent and carefully planned out everything you need, so all that’s left is to execute."
    teacher "However, you need to keep in mind one last thing: your own limitations."
    call rngteachingscene from _call_rngteachingscene_194
    teacher "When I first started out as a feedee, it wasn’t with massive feast of fried chicken or chugging down dozens of milkshakes."
    teacher "I needed something that properly fit with my tiny tummy."
    teacher "Your first time doing a binge session should be kept to a relatively small scale."
    call rngteachingscene from _call_rngteachingscene_195
    teacher "Try downing a single pizza by yourself with the option of a couple scoops of ice cream if you feel like you could go a little further."
    teacher "Pushing yourself too far can have dire consequences on your body. Stomach aches, bathroom troubles, and similarly unpleasant issues."
    call rngteachingscene from _call_rngteachingscene_196
    teacher "There’s also the monetary issues of blowing all of your cash on a surplus of food you can never eat."
    teacher "After going through the trouble of warming up a dozen boxes of fried chicken in the microwave, it doesn’t matter when you end up having to throw it all away once you’ve hit your breaking point."
    call rngteachingscene from _call_rngteachingscene_197
    teacher "As you go on and increase your appetite, that’s when you can start taking on larger portion sizes. Think of it as a long term goal to be able to eat a table’s worth of food by yourself."
    teacher "It all starts with the single step of starting small to give your body a chance to grow along with your ambitions."
    $ teaching_feederfeedee_times = 3
    return

label feeder_feedee4:
    #Part 4: Living the Lifestyle
    call rngteachingscene from _call_rngteachingscene_198
    teacher "Before we completely move away from the discussion about a feedee feeder relationships, I would like to emphasize something."
    teacher "This class may have given you an incorrect impression of what the lifestyle is all about."
    call rngteachingscene from _call_rngteachingscene_199
    teacher "Based off of what I’ve shown and what can be seen in a lot of material online, it appears at a glance that it’s an all or nothing kind of situation."
    teacher "You either starving yourself to build up your hunger or you’re ending every session doing an impression of a bloated, beached whale."
    teacher "I’m here to tell you that not everyone goes that hard in the lifestyle. Everyone has their own preferences for how deep they want to go."
    call rngteachingscene from _call_rngteachingscene_200
    teacher "It could be as simple as planning a stuffing session with your significant other once a month. Treat it as a stress relief session to burn off some anxiety in exchange for putting on the pounds."
    teacher "Going back to our portion talk, this also gives you a chance to save up and carefully pick out what you want to gorge on. It all depends on your personal preferences."
    call rngteachingscene from _call_rngteachingscene_201
    teacher "My final point is that this lifestyle doesn’t have to define your entire personality. You can choose to go whole hog into it, or just leave it as a fun hobby you indulge in every once in a while."
    teacher "You can probably tell which of the two I prefer, but that’s my choice to make. At the end the day, what you choose to be comfortable with doing is all dependent on your own choices."
    $ teaching_feederfeedee_check = 1
    return

label fatphobia1:
    #Part 1: Overview
    call rngteachingscene from _call_rngteachingscene_202
    teacher "A few of you have brought to my attention your concerns regarding my weight gain. While I appreciate that you care about my health, I feel like there’s more to it than just that."
    teacher "When I initially announced the drastic change in my teaching methods, no doubt a few of you began to have second thoughts. You probably thought I had gone insane."
    call rngteachingscene from _call_rngteachingscene_203
    teacher "This all stems from a societal expectation that being overweight is inherently bad. This can be properly summarized in one word: Fatphobia."
    teacher "For those of you that are unaware, phobia is used to describe a specific fear. In this case an aversion to fat."
    call rngteachingscene from _call_rngteachingscene_204
    teacher "This doesn’t mean people are actually terrified of fat people. More so that they see gaining weight and overweight individuals in a negative perception."
    teacher "Like you, some of this comes from genuine concern of the self and others. However, the widespread effects of this phenomenon have created a plethora of issues."
    teacher "Issues that will take a bit more time than what we have today unfortunately. We’ll have to continue next time."
    $ teaching_fatphobia_times = 1
    return

label fatphobia2:
    #Part 2: Fat Characters in Media
    call rngteachingscene from _call_rngteachingscene_205
    teacher "Let me ask you something. Whenever you see a fat person in a movie, tv show, or any other piece of media, what are they usually portrayed as?"
    teacher "More than likely, they fall into certain stereotypes. They could be the bumbling, comedic relief that gets mocked for their weight and appetite."
    teacher "A greedy businessperson that gorges themselves on food at the expense of others."
    call rngteachingscene from _call_rngteachingscene_206
    teacher "An ugly, bastard of a fat man that takes advantage of a young woman to satisfy his-"
    "Daisy pauses for a moment, realizing what she’s about to say."
    teacher "Er, maybe best not to bring that up in class, but you get my point."
    call rngteachingscene from _call_rngteachingscene_207
    teacher "In any case, I think I’ve proven my point that obese people aren’t given the kindest treatment when it comes to fiction."
    teacher "It’s very rare to have a lead character be anything other than slim or toned."
    call rngteachingscene from _call_rngteachingscene_208
    teacher "This all goes back to what the public sees as acceptable bodies to glorify and which ones to condemn."
    teacher "All of this because of a perceived expectation for fat people to be lazy and in bad health."
    call rngteachingscene from _call_rngteachingscene_209
    teacher "While that’s far from reality, it’s unfortunately the one created by the entertainment industry."
    teacher "It’s something that’s gotten better over the years, but still needs a bit of work to make people feel comfortable in their larger sizes being represented on a screen."
    $ teaching_fatphobia_times = 2
    return

label fatphobia3:
    #Part 3: Health Concerns
    call rngteachingscene from _call_rngteachingscene_210
    teacher "One of the major factors contributing to fatphobia is the idea that being fat automatically equates to being unhealthy."
    teacher "I’m sure you’ve seen horror stories on reality TV of people bound to beds or having to go through with risky heart surgery because of their excess weight."
    teacher "While it is true that fat can cause these issues, it’s not always the case."
    call rngteachingscene from _call_rngteachingscene_211
    teacher "Weight can be put on safely if a person manages to eat right and remain active to keep themselves in a state that keeps up with their added bulk."
    teacher "This notion also fails to consider those that are naturally born fat and are incapable of taking it off easily due to genetics or their own metabolism."
    call rngteachingscene from _call_rngteachingscene_212
    teacher "People wanting to help those that are dealing with health issues associated with obesity are trying to do the right thing. I won’t deny that."
    teacher "However, they fail to see the long term side effects that their fatphobia can cause, not just to fat people, but to our society as a whole."
    $ teaching_fatphobia_times = 3
    return

label fatphobia4:
    #Part 4: Negative Effects of Fatphobia
    call rngteachingscene from _call_rngteachingscene_213
    teacher "We’ve spent several classes now talking about the effects of fatphobia. However, I’ve failed to accurately explain the extent of how it has affected our society."
    teacher "First and foremost, it has led to mistreatment for anyone that dares to go to the plus-sized section of a store just to find something that fits."
    call rngteachingscene from _call_rngteachingscene_214
    teacher "Constant fat shaming and ridicule can lead to a poor self-esteem that could end up hurting these people in the long run."
    teacher "Even people that aren’t fat suffer from the consequences. Those with acute fear of gaining weight or are peer pressured to be as skinny as possible sometimes develop eating disorders."
    call rngteachingscene from _call_rngteachingscene_215
    teacher "They’re so terrified of putting on a single pound that they’re likely to go days without eating to the point of collapsing."
    teacher "I don’t know about you, but I’d rather lug around a few extra pounds than suffer the side effects of being nothing, but skin and bones."
    call rngteachingscene from _call_rngteachingscene_216
    teacher "So please, be sure to treat those that are larger than you as equal, not pariahs. Do it for the betterment of, not only them, but for the human race as a whole."
    $ teaching_fatphobia_check = 1
    return

label socialfood1:
    #Part 1: Eating Out
    call rngteachingscene from _call_rngteachingscene_217
    teacher "Let me ask you all something. When you go out to eat, is it usually by yourself?"
    teacher "Odds are that most of your trips to restaurants have involved being joined by other people."
    teacher "Friends, family, coworkers, or anyone else that are a part of your social circles."
    call rngteachingscene from _call_rngteachingscene_218
    teacher "This pattern works into an aspect that plays a big part in how and what we eat."
    teacher "For instance, you might be more inclined to try out more food if it means sharing it amongst friends."
    teacher "Whether that be sampling a few bites from their plate or finishing up whatever they leave behind."
    call rngteachingscene from _call_rngteachingscene_219
    teacher "There’s always the trap of ordering dessert for the group with the intention of sharing it."
    teacher "While that is true, most of the time there will always be that one person that takes a little more than everyone else."
    call rngteachingscene from _call_rngteachingscene_220
    teacher "Whether intentional or not, this all leads to opportunities for gluttons to really indulge themselves while simultaneously accomplishing the human need to feel like you belong."
    teacher "Sure people might mock you behind your back if you decide to pig out at a buffet all by yourself."
    call rngteachingscene from _call_rngteachingscene_221
    teacher "However, at least if you’re among the right crowd, they could actually cheer you on to show pride for your unbridled appetite."
    teacher "Perhaps one day I’ll bring the entire class to a restaurant as a celebration for your hard work."
    call rngteachingscene from _call_rngteachingscene_222
    teacher "Don’t worry, I’ll be sure to cover the bill. Needless to say, I’m going to spend the session ordering everything off of the menu."
    $ teaching_socialfood_times = 1
    return

label socialfood2:
    #Part 2: Parties
    call rngteachingscene from _call_rngteachingscene_223
    teacher "Whenever someone wants to do a proper celebration, there’s usually one thing that comes to mind: a party."
    teacher "Everything from a small gathering of office workers to celebrate the end of the week or a massive reception to properly send off a wedding."
    call rngteachingscene from _call_rngteachingscene_224
    teacher "Parties are the perfect place for people to socialize with friends both old and new to enjoy themselves."
    teacher "However, a party needs a few things in order to be fully realized. Things like a venue and guests."
    teacher "Of particular importance is the need to provide ample food and drink."
    call rngteachingscene from _call_rngteachingscene_225
    teacher "People can’t dance if there’s nothing to fuel their bodies and their throats will get dry from talking with nothing to quench their thirst."
    teacher "In this kind of atmosphere, it’s expected to see a plethora of different food stuffs either provided by the host or put together by the guests themselves."
    call rngteachingscene from _call_rngteachingscene_226
    teacher "Cakes, appetizers, soda, alcohol, sandwiches, pizza, homemade, and catering orders from your favorite eateries are all great additions to any party."
    teacher "Seeing this kind of spread in person is typically more than enough to overwrite our national hunger inhibitors."
    call rngteachingscene from _call_rngteachingscene_227
    teacher "Too busy conversing with others and having a good time, you might forget to watch what you’re eating."
    teacher "If you’re not careful, you could wake up the next morning in a strange bed with a stuffed belly that’s about to pop."
    call rngteachingscene from _call_rngteachingscene_228
    teacher "You might even find someone cuddling up to your stuffed tummy that had a part in giving you such an enjoyable evening."
    ms "Wait, did this all happen to you before?"
    teacher "Er, I think that’s enough for today’s class. I’ll see you all next time."
    $ teaching_socialfood_times = 2
    return

label socialfood3:
    #Part 3: Being Cozy
    call rngteachingscene from _call_rngteachingscene_229
    teacher "Let’s say you’ve been quite the social butterfly for a week straight. If you weren’t out a restaurant entertaining your fellow employees, you were at a party to join in on the celebrations."
    teacher "By the end of that endurance run, your social battery might be running on empty."
    call rngteachingscene from _call_rngteachingscene_230
    teacher "In this case, it might be better to say no to a few invitations to give yourself a chance to recharge. Not that you have to fully commit to being along to do so."
    teacher "I will admit, being by yourself is sometimes a relief, but there’s a certain charm of enjoying the company of a single person that cares about you."
    teacher "The kind of partner that is more than willing to waste away a Friday night on the couch watching TV."
    call rngteachingscene from _call_rngteachingscene_231
    teacher "Either in your raggedy clothes, bundled up in a blanket, or wearing nothing at all. It’s not like you have anything to hide from each other."
    teacher "In these kinds of situations, the likelihood for the two of you to forgo actual cooking in favor of ordering out is at an all-time high."
    teacher "Your combined laziness typically overlooks the health concerns for such a meal in favor of doing whatever’s easiest and appealing to your bellies."
    call rngteachingscene from _call_rngteachingscene_232
    teacher "Left with only yourself, a partner, and a selection of unhealthy food to munch on, all that remains is to completely engulf yourself in relaxation."
    teacher "Spending the evening watching something on your preferred screen while you mindlessly stuff yourself."
    teacher "Whether or not this leads to a more “intimate” form of being together is all up to what you’re feeling that evening and whether or not your body can move after your earlier indulgence."
    call rngteachingscene from _call_rngteachingscene_233
    teacher "Regardless, it’s a great way to recuperate from the challenges of social interaction while still maintaining the basic human need of belonging."
    teacher "Even if it’s only with the one person that matters most to you."
    $ teaching_socialfood_check = 1
    return

label clothing1:
    #Part 1: Introduction
    call rngteachingscene from _call_rngteachingscene_234
    teacher "We’ve gone out of our way to explain the beauty of larger bodies. However, it’s not like overweight people are expected to bare it all when they step out of the house."
    teacher "Now most of you may make the obvious connection that I’m talking about clothing."
    teacher "While that is true, it’s not as simple as walking into a store to try out a bunch of different outfits."
    call rngteachingscene from _call_rngteachingscene_235
    teacher "More often than not, the major outlets’ selection of plus-sized clothing is very small in terms of selection."
    teacher "Even then, they may not have anything that properly fits or works well with certain body shapes."
    call rngteachingscene from _call_rngteachingscene_236
    teacher "While there are stores that specialize in certain types of clothing, both online and physical, there also comes the issue of figuring out what fits."
    teacher "I’ve faced this struggle myself multiple times."
    call rngteachingscene from _call_rngteachingscene_237
    teacher "Though I did have to suffer through these challenges, it also means that I’ve gained knowledge on how to help out anyone else that takes on this task."
    teacher "I’ll be more than happy to share these tips with you…next time. This lesson is going to need quite a few sessions to get through."
    $ teaching_clothing_times = 1
    return

label clothing2:
    #Part 2: Undergarments
    call rngteachingscene from _call_rngteachingscene_238
    teacher "Let’s start off the conversation of plus-sized clothing with what most people usually start with when getting dressed: undergarments."
    teacher "Though they’re not something you typically want to show off in public, that doesn’t make them any less important."
    teacher "They’re crucial to keeping things in place and comfortable as you go about your day."
    call rngteachingscene from _call_rngteachingscene_239
    teacher "Typically, a person’s method of procuring underwear is dependent on the style they’re looking for."
    teacher "Either going to a lingerie store for something sexy or just buying a bulk pack of white undies as an example."
    teacher "For larger people, this is where the first of their issues come up."
    call rngteachingscene from _call_rngteachingscene_240
    teacher "Because sometimes if you find something that fits, it’s not the most appealing to the eye."
    teacher "On the reverse, you may find something that fits perfectly that looks bland and leaves a lot to be desired."
    call rngteachingscene from _call_rngteachingscene_241
    teacher "You have to be very careful when it comes to filling up your undergarment collection because of this."
    teacher "As a quick tip, if you find something that fits and that you like the look of, make sure pick up duplicates of it on the spot."
    call rngteachingscene from _call_rngteachingscene_242
    teacher "You never know when you’ll find such a treasure again. Needless to say, these things can only survive so much wear and tear from everyday life."
    teacher "Well, and certain other things that I can’t talk about in class."
    $ teaching_clothing_times = 2
    return

label clothing3:
    #Part 3: Tips for Plus-Sized Clothes Shopping
    call rngteachingscene from _call_rngteachingscene_243
    teacher "Let’s say you’ve decided to venture into a new store. Your goal: find something that will fit a person of a larger size."
    teacher "First of all, I applaud you for taking on this challenge. Second, allow me to give you some general tips to help you through the ordeal."
    call rngteachingscene from _call_rngteachingscene_244
    teacher "An obvious one to start with is useful for any trip to a clothing store. Make sure you plan ahead with a budget in mind."
    teacher "Though some plus-sized clothing may come with a hefty price tag, you need to have the discipline to know when to save your wallet for the next feeding session."
    call rngteachingscene from _call_rngteachingscene_245
    teacher "Once you arrive at the store, don’t just grab the first thing you see that boasts a seemingly perfect size label. Grab a couple of outfits and then make your way to a changing booth."
    teacher "This will give you plenty of opportunities to try out different styles and sizes to get an idea of what you’re working with."
    teacher "Bonus points if you have a partner that understands your tastes well enough to grab more clothes while you’re trying the first sets on."
    call rngteachingscene from _call_rngteachingscene_246
    teacher "Once you’ve pinned down how the store classifies their sizes in relation to how well they actually fit your body, the time comes to make your decision."
    teacher "With your reconnaissance complete, you should be able to take your time going over what options are available to you."
    call rngteachingscene from _call_rngteachingscene_247
    teacher "After all, shopping is supposed to be a leisurely activity. Remain calm and enjoy yourself as you find the perfect outfit to really emphasize your curves."
    teacher "The only caveat is that your actual experience will vary greatly depending on which store you choose. Perhaps next time I can give you some suggestions."
    $ teaching_clothing_times = 3
    return

label clothing4:
    #Part 4: The FOH Clothing Store
    call rngteachingscene from _call_rngteachingscene_248
    teacher "I’d like to end our discussion on plus-sized clothing by providing an easy route for anyone on the search for outfits for the overweight."
    teacher "Recently, I’ve happened upon a website owned by a company known as FOH. I had never heard about the online shop before, but they were able to catch my eye in a matter of seconds."
    call rngteachingscene from _call_rngteachingscene_249
    teacher "Scrolling through their site provided me with hundreds upon hundreds of different options for larger ladies like me. Each of them looked so cute and claimed to perfectly fit any proportions."
    teacher "Curious, I ordered myself a few of their offerings and was pleasantly surprised. True to their word, I have yet to find an outfit I haven’t absolutely loved."
    call rngteachingscene from _call_rngteachingscene_250
    teacher "In addition to their selection, they also offer general tips for obese people and those wishing to better “fill out” their clothes."
    teacher "I would highly recommend visiting it, not only for the online store, but also for their wealth of information about the topic. I promise, you won’t be disappointed."
    $ teaching_clothing_check = 1
    return

label gaining_tips1:
    #Part 1: The Diet
    call rngteachingscene from _call_rngteachingscene_251
    teacher "I would like to broach the topic on how to gain weight with a very important piece of the puzzle."
    teacher "Just like how a construction worker needs tools and a painter needs a brush, there is something vital to this procedure."
    teacher "In our case, that would be food and drinks."
    call rngteachingscene from _call_rngteachingscene_252
    teacher "While you may think it’s just a matter of stuffing yourself with whatever you can grab, the best results are achieved by modifying your diet to meet your goals."
    teacher "A easy addition to your meals is anything high in carbs. Things such as bread, pasta, or potatoes can really give your body the fuel it needs to pack on the pounds."
    call rngteachingscene from _call_rngteachingscene_253
    teacher "In addition, having a lot of meat in your diet provides plenty of protein to work with. I’m mostly talking about red meats such as beef, pork, or lamb."
    teacher "Needless to say, foods high in sugar are also excellent to consider when prioritizing growth. Just make sure you don’t go too crazy, or your teeth may rot."
    call rngteachingscene from _call_rngteachingscene_254
    teacher "Keep in mind, that these suggestions are more for a general audience. How they actually alter your body can vary from person to person."
    teacher "Of course, you need to make sure you enjoy what you’re eating since that’s a major factor for this lifestyle. Pick out whatever works best for you."
    teacher "There’s nothing quite like letting yourself go wild on a feast made up of your most favorite foods."
    $ teaching_gainingtips_times = 1
    return

label gaining_tips2:
    #Part 2: Partner Support
    call rngteachingscene from _call_rngteachingscene_255
    teacher "While it is entirely possible to gain under your own power, you can never underestimate the advantages of having someone along for the ride."
    teacher "Whether it’s a significant other, a professional, or just a really open minded friend, having an extra set of hands can be crucial to pushing you past your limits."
    call rngteachingscene from _call_rngteachingscene_256
    teacher "This can range from simply aiding you in carrying in massive food deliveries to helping you clean up when everything is done."
    teacher "As to be expected, the bulk of their assistance is truly appreciated during the stuffing sessions themselves."
    teacher "Physically speaking, they can aid in your digestion by rubbing your distended belly."
    call rngteachingscene from _call_rngteachingscene_257
    teacher "They can also help shove that last bit of food down your throat while keeping your physical limitations in mind."
    teacher "However, even if they can’t do any of that, just them being there for mental support is enough to show drastic results."
    call rngteachingscene from _call_rngteachingscene_258
    teacher "A few sweet words glorifying your gluttony or a harsh command from a more dominating partner tend to help you go that extra mile."
    teacher "Then again, make sure you’ve properly talked to your feedee before any of this occurs. You never know when your stuffing session might end up pushing them beyond their own limits."
    $ teaching_gainingtips_times = 2
    return

label gaining_tips3:
    #Part 3: Methods
    call rngteachingscene from _call_rngteachingscene_259
    teacher "When it comes to increasing your appetite, it’s similar to keeping up with a regular exercise routine."
    teacher "You need to pin down the specifics on how you do it to produce the best results."
    teacher "One quick tip is to never stop eating. This means that between your regularly scheduled meals that you keep snacking to keep up your appetite."
    call rngteachingscene from _call_rngteachingscene_260
    teacher "Even if it’s something small like chips or crackers, make sure your mouth is constantly chewing or drinking something."
    teacher "During the actual stuffing process, have plenty of water or soda on hand. The beverages can help soften up the food to make it fit better in your belly."
    call rngteachingscene from _call_rngteachingscene_261
    teacher "Though it might sound gross, especially if you have to do it in front of your partner, you also want to let out any burps."
    teacher "The release should help free up room to help you squeeze in that last little bit."
    call rngteachingscene from _call_rngteachingscene_262
    teacher "These are just scratching the surface of different ways you can help along your journey, but they’re the ones that I’ve found most effective for me."
    teacher "Well, and one more thing that we’ll cover next time."
    $ teaching_gainingtips_times = 3
    return

label gaining_tips4:
    #Part 4: Having Fun
    call rngteachingscene from _call_rngteachingscene_263
    teacher "Finishing up my little crash course on gaining tips, I would like to go over what could possibly be one of the more important factors: having fun."
    teacher "Sure, you could get results if you go through flavorless bowls of grease and gruel, but I doubt you would enjoy it very much."
    call rngteachingscene from _call_rngteachingscene_264
    teacher "Even if you do get the body you’re looking for, the path to get there might leave you with enough regret to want to undo all of your hard work."
    teacher "Gaining weight is definitely a case of appreciating the journey just as much, if not more, as the destination."
    teacher "You need to make sure that every step away fulfills your needs and leaves you excited for what’s to come."
    call rngteachingscene from _call_rngteachingscene_265
    teacher "Perhaps you change up how you take the food. Things like trying out funnel feeding or acting like a little piggy and setting up a makeshift feeding trough."
    teacher "Even if the method isn’t much different, getting to play out scenarios with your partner can add some much needed spice to the event."
    call rngteachingscene from _call_rngteachingscene_266
    teacher "Think like a queen being waited on hand and foot by her loyal servant or a bad school girl being force fed as punishment."
    teacher "The point being, that you want to make memories alongside making massive gains. It’s your body and your chance to really shape it into a form that brings you the most happiness."
    $ teaching_gainingtips_check = 1
    return


label lyn_guest_lecture:
    call rngteachingscene
    teacher "I have a special guest today to talk to you about her experience with streaming as a plus-sized streamer."
    teacher "Please give a warm welcome to Ms. Luxury Leanne."
    image lyn_lecture_1 = "/leanne/events/stage13/lyn_lecture1.webp"
    scene lyn_lecture_1
    "Walking in from outside of the hall, Lyn takes her place at the front of the class."
    image lyn_lecture_2 = "/leanne/events/stage13/lyn_lecture2.webp"
    scene lyn_lecture_2
    leanne "Actually, I just go by Lyn. Part of a new image I’ve been trying to use."
    teacher "I apologize. Alright Ms. Lyn, would you mind telling the class what you do for a living?"
    image lyn_lecture_3 = "/leanne/events/stage13/lyn_lecture3.webp"
    scene lyn_lecture_3
    leanne "I’m a streamer. I spend most of my evenings playing games and hanging out with people online."
    leanne "Outside of that, I deal with the various technical aspects of the job and try to think of new ideas to entertain my viewers."
    teacher "And how has being on the larger side affected this?"
    image lyn_lecture_4 = "/leanne/events/stage13/lyn_lecture4.webp"
    scene lyn_lecture_4
    leanne "There have been some less than savory people that have tried to use my heavier figure to try and insult me."
    leanne "Thankfully, that’s been drowned out by an overwhelming outpour of support."
    teacher "Has your career had a direct impact on your weight?"
    image lyn_lecture_5 = "/leanne/events/stage13/lyn_lecture5.webp"
    scene lyn_lecture_5
    leanne "It started off with people sending in pizza donations, but it admittedly got a little out of hand."
    leanne "Now it seems like people tune in mostly to see me stuff myself."
    teacher "And are you okay with this lifestyle?"
    image lyn_lecture_6 = "/leanne/events/stage13/lyn_lecture6.webp"
    scene lyn_lecture_6
    leanne "It’s admittedly a bit different than what I originally envisioned, but yeah."
    leanne "Getting over some hurdles allowed me to discover who I was. I’m hoping that I can help others do the same with my streams."
    teacher "Thank you so much for your time."
    image lyn_lecture_7 = "/leanne/events/stage13/lyn_lecture7.webp"
    scene lyn_lecture_7
    leanne "My pleasure."
    image lyn_lecture_8 = "/leanne/events/stage13/lyn_lecture8.webp"
    scene lyn_lecture_8
    "Giving you a subtle wave as she leaves, Lyn exits out the door to let Daisy retake her position at the head of the class."
    call rngteachingscene
    teacher "I hope you all enjoyed the presentation today. Class is dismissed."

    image lyn_lecture_9 = "/leanne/events/stage13/lyn_lecture9.webp"
    scene lyn_lecture_9
    "On your way out, you spot Lyn standing nearby and decide to go talk to her."
    image lyn_lecture_10 = "/leanne/events/stage13/lyn_lecture10.webp"
    scene lyn_lecture_10
    leanne "I had no idea you were in this class, but I was glad to see a familiar face. I helped keep my nerves at bay."
    pc "Don’t you stream all the time?"
    image lyn_lecture_11 = "/leanne/events/stage13/lyn_lecture11.webp"
    scene lyn_lecture_11
    leanne "Yeah, but never in front of a live audience."
    leanne "It was a bit strange doing my usual performance IRL, but I think I did a good enough job. What do you think?"
    pc "I think you were great."
    image lyn_lecture_12 = "/leanne/events/stage13/lyn_lecture12.webp"
    scene lyn_lecture_12
    leanne "Thank you. Want to go grab a bite to eat? I’m a little hungry after all of that."
    menu:
        "Okay. Let's go to The Sugar Shop.":
            call lyn_date_sugarshop
        "Sorry, I'm busy.":
            leanne "Alright. I’ll catch you some other time then."
            "You head home for the day."
    stop music fadeout 1.0
    $ teaching_leanneguest = 1
    return

label leanne_guest_lecture:
    call rngteachingscene
    teacher "I have a special guest today to talk to you about her experience with streaming as a plus-sized streamer."
    teacher "Please give a warm welcome to Ms. Luxury Leanne."
    image leanne_lecture_1 = "/leanne/events/stage13/leanne_lecture1.webp"
    scene leanne_lecture_1
    "Walking in from outside of the hall, Leanne strikes a pose as she stands in front of the class."
    image leanne_lecture_2 = "/leanne/events/stage13/leanne_lecture2.webp"
    scene leanne_lecture_2
    window hide
    pause
    image leanne_lecture_3 = "/leanne/events/stage13/leanne_lecture3.webp"
    scene leanne_lecture_3
    leanne "Thank you Ms. Tanwen. Haven’t done IRL shows in a while so I’m excited to see how this goes."
    teacher "I’m glad to hear that. Alright Ms. Leanne, would you mind telling the class what you do for a living?"
    image leanne_lecture_4 = "/leanne/events/stage13/leanne_lecture4.webp"
    scene leanne_lecture_4
    leanne "I’m a streamer that spends her nights playing games, stuffing herself silly, and indulging in other fun stuff for the sake of entertaining the masses."
    teacher "And how has being on the larger side affected this?"
    image leanne_lecture_5 = "/leanne/events/stage13/leanne_lecture5.webp"
    scene leanne_lecture_5
    leanne "Great! Having a plump body like this makes me stand out from the usual crowd."
    leanne "Not to mention all the extra fun things I can do with it. Whether that’s binging on delicious food or performing “other” activities."
    teacher "Has your career had a direct impact on your weight?"
    image leanne_lecture_6 = "/leanne/events/stage13/leanne_lecture6.webp"
    scene leanne_lecture_6
    leanne "Absolutely. It all started off as people sending me pizza donations and from there it spiraled into full-on feeding streams."
    leanne "They rake in the views, especially when I decide to get a little naughty."
    teacher "And are you okay with this lifestyle?"
    image leanne_lecture_7 = "/leanne/events/stage13/leanne_lecture7.webp"
    scene leanne_lecture_7
    leanne "Absolutely. I’ve never felt so free before. Best of all, I get to share the fun with countless viewers that adore me."
    leanne "I wouldn’t give it up for anything in the world."
    teacher "That’s excellent to hear. Thank you so much for coming today."
    image leanne_lecture_8 = "/leanne/events/stage13/leanne_lecture8.webp"
    scene leanne_lecture_8
    leanne "You’re welcome. I hope you all decide to tune in to one of my streams sometime. Until then, this is Luxury Leanne signing off!"
    image leanne_lecture_9 = "/leanne/events/stage13/leanne_lecture9.webp"
    scene leanne_lecture_9
    "Pausing a bit to give out autographs to some of the students, Leanne gives you a subtle wave before taking her leave."
    call rngteachingscene
    teacher "I hope you all enjoyed the presentation today. Class is dismissed."

    image leanne_lecture_10 = "/leanne/events/stage13/leanne_lecture10.webp"
    scene leanne_lecture_10
    "On your way out, you spot Leanne standing nearby and decide to go talk to her."
    image leanne_lecture_11 = "/leanne/events/stage13/leanne_lecture11.webp"
    scene leanne_lecture_11
    leanne "Didn’t expect to see one of my biggest fans here. Especially since it was my first time doing that in front of people."
    pc "Don’t you stream all the time?"
    image leanne_lecture_12 = "/leanne/events/stage13/leanne_lecture12.webp"
    scene leanne_lecture_12
    leanne "I mean doing it in-person. It’s completely different doing my stuff when I can actually see my viewers ogling my body."
    leanne "I know I looked good, but how was my presentation?"
    pc "I think you were great."
    image leanne_lecture_13 = "/leanne/events/stage13/leanne_lecture13.webp"
    scene leanne_lecture_13
    leanne "Aww thank you. I think I’ve earned myself a little treat. Want to join me somewhere for a snack?"
    menu:
        "Sure. Let's head to Bunny Bites.":
            call leanne_feeding_bunnybites
        "Sorry, I'm busy.":
            leanne "Alright. I’ll catch you some other time then."
            "You head home for the day."
    stop music fadeout 1.0
    $ teaching_leanneguest = 1
    return


label gabe_guest_lecture:
    #BONUS Gabe Guest Speaker Lesson
    #(NOTE: This could occur as a random lesson event after Lyn/Leanne’s stage 16 event)
    #IMAGE: Daisy standing in front of the class.
    teacher "I have another guest speaker lined up for you all today. Please give a warm welcome to Mr. Gabe."
    #IMAGE: Gabe standing in front of the class.
    "Hearing his call, Gabe shuffles into the room. Judging by the expression on his face, he seems just as confused as the rest of the class."
    gabe "Uh, hey?"
    teacher "Thank you for coming in today Mr. Gabe. Now could you tell the class what you do for a living?"
    gabe "Okay, I run the Anime Shop downtown."
    teacher "And is that it?"
    gabe "Yeah? I just spend my time working the cash register and restocking shelves."
    teacher "Alright. And how has your larger body affected your ability to work?"
    gabe "I mean…I can’t wear certain shirts we sell since they don’t come in my size. Why does that matter?"
    teacher "This class is trying to study the effects of weight gain on people’s livelihoods."
    gabe "That’s weird."
    teacher "Er, let’s move on. What made you decide to want to live on the larger side?"
    gabe "What are you on about? Being fat wasn’t a choice. Just a matter of lack of motivation to exercise and a slow metabolism."
    gabe "You reach my age and stress is bound to get you too."
    teacher "Um, it seems I might have made a mistake. Well, thank you for your time Mr. Gabe."
    gabe "Right. If any of you are interested, feel free to stop by the shop if you’re looking for something specific."
    gabe "Just got some rare items in stock too. Like Hentai Harem Hijinx Volume-"
    teacher "Thank you very much Mr. Gabe! Have a good day."
    #IMAGE: A nervous Daisy standing in front of the class.
    "After pushing Gabe out the door and closing it behind him, Daisy returns to the front of the class."
    teacher "Well, that didn’t go as expected. Let’s just call it for today."
    teacher "I’ll…try to ask my guests clearer questions before requesting them to speak to the class next time."
    $ teaching_gabeguest = 1
    return

label teaching_bmi:
    image stage_7_event_10 = "/teacher/events/stage7/10.webp"
    scene stage_7_event_10
    "You see Ms. Tanwen standing at the front of the classroom, adjusting her glasses as she prepares to speak."
    "Her warm smile makes the lecture feel more like a casual conversation than a lesson."
    image stage_7_event_11 = "/teacher/events/stage7/11.webp"
    scene stage_7_event_11
    teacher "Alright, class, today we're going to talk about BMI. Body Mass Index."
    teacher "It's a simple number that helps categorize body weight. Anyone know how we calculate it?"
    "A few students murmur, but no one gives a clear answer."
    teacher "No worries! BMI is calculated using a person's weight in kilograms divided by the square of their height in meters."
    teacher "The formula is BMI equals weight over height squared. Simple, right?"
    image stage_7_event_12 = "/teacher/events/stage7/12.webp"
    scene stage_7_event_12
    "She writes the formula on the board."
    #BMI = weight (kg) / height (m²)
    image stage_7_event_13 = "/teacher/events/stage7/13.webp"
    scene stage_7_event_13
    teacher "Now, before we go further, let's be clear. BMI is just one way to measure body size, but it doesn't tell the whole story."
    teacher "It doesn't consider muscle mass, bone density, or fat distribution. However, it's a useful starting point for understanding weight categories."
    image stage_7_event_14 = "/teacher/events/stage7/14.webp"
    scene stage_7_event_14
    teacher "For example, BMI is divided into categories."
    teacher "A BMI below 18.5 is considered underweight. A BMI between 18.5 and 24.9 is considered normal weight."
    teacher "Then we have overweight at 25 to 29.9, and obesity starts at 30. We even classify obesity into different classes."
    teacher "Class I is 30-34.9, Class II is 35-39.9, and Class III, which some call 'severe obesity,' is 40 or higher."
    teacher "While originally these three obesity classes were enough to define most cases, we have become a lot fatter as a society in the last twenty years."
    teacher "So you now also have Class IV which is a BMI of 40 to 50, and Class V obesity which is a BMI of 50 or higher."
    image stage_7_event_15 = "/teacher/events/stage7/15.webp"
    scene stage_7_event_15
    "She pauses to let it sink in before continuing."
    teacher "Now, let's talk about why BMI exists and what it is used for."
    teacher "The most common use for BMI is to assess how far the individual's body weight departs from what is normal for a person's height."
    teacher "This allows health care professional to quickly identify if you are underweight or overweight for your height."
    teacher "With this information the health care professional can recommend you a suitable solution if they deems the value to be too far from the norm."
    teacher "You might think that a higher then normal BMI would automatically mean that the person in question is eating too much food."
    teacher "But, a body with a high amount of muscularity could also fall into the obese category."
    teacher "Besides that, there are genetic, environmental, and behavioral factors involved."
    teacher "Did you know that more than 140 genetic regions have been linked to obesity? That means some people are predisposed to gain weight more easily."
    image stage_7_event_16 = "/teacher/events/stage7/16.webp"
    scene stage_7_event_16
    "You see a few students nodding, intrigued."
    teacher "Now with all that in mind, you can see that BMI does not tell you everything. In many ways it is a flawed metric."
    teacher "There are a few alternative metrics, that are more rigorous and based on more then just weight and height."
    teacher "Currently, almost everywhere BMI is still the most used, so I won't go into the other metrics here."
    "She glances at the clock before finishing."
    image stage_7_event_17 = "/teacher/events/stage7/17.webp"
    scene stage_7_event_17
    teacher "The key takeaway? BMI is a tool, not a perfect measure. Everyone's body is different, and health isn't just about numbers."
    teacher "It's about lifestyle, genetics, and personal goals. Any questions?"
    $ renpy.notify("BMI unlocked in stat screen.")
    $ teaching_bmi_check = 1
    return
    
label teaching_bodyfat:
    image stage_8_event_16 = "/teacher/events/stage8/16.webp"
    scene stage_8_event_16
    "You see Ms. Tanwen standing at the front of the classroom once again, her usual warm smile greeting the students." 
    image stage_8_event_17 = "/teacher/events/stage8/17.webp"
    scene stage_8_event_17
    teacher "Alright, class, we talked about BMI before." 
    teacher "Today, we're going to talk about something closely related but quite different. Body fat percentage." 
    teacher "Can anyone tell me how it's different from BMI?"
    image stage_8_event_18 = "/teacher/events/stage8/18.webp"
    scene stage_8_event_18
    "A few students exchange glances before someone hesitantly raises a hand." 
    ms "BMI just uses height and weight, but body fat is more specific?"
    "Ms. Tanwen nods approvingly." 
    image stage_8_event_19 = "/teacher/events/stage8/19.webp"
    scene stage_8_event_19
    teacher "Exactly! BMI is a general measure of body size, but it doesn't tell us how much of our weight is fat versus muscle, bone, or water." 
    teacher "That's where body fat percentage comes in. It's a much more detailed look at body composition."
    image stage_8_event_20 = "/teacher/events/stage8/20.webp"
    scene stage_8_event_20
    "She turns to the board and writes."
    #Body Fat Percentage = (Fat Mass / Total Body Mass) x 100
    image stage_8_event_21 = "/teacher/events/stage8/21.webp"
    scene stage_8_event_21
    teacher "So, while BMI categorizes people into underweight, normal weight, overweight, and obesity classes, body fat percentage gives us a better idea of actual fat levels." 
    teacher "Generally, for men, a healthy body fat range is 10-20 percent, and for women, it's 18-28 percent." 
    teacher "Athletes tend to have lower numbers, while higher numbers can indicate excess fat storage."
    teacher "Now, how do we measure body fat? There are several ways. Some are simple, like skinfold calipers, which pinch the skin to estimate fat under it." 
    teacher "Others, like bioelectrical impedance scales, send a weak electrical current through the body to estimate fat percentage." 
    teacher "The most accurate methods are DEXA scans and hydrostatic weighing, but those are expensive and not as commonly used."
    image stage_8_event_22 = "/teacher/events/stage8/22.webp"
    scene stage_8_event_22
    teacher "So, why does this matter? Well, when we know the body fat percentage we also know how much of the body is not fat." 
    teacher "We call this lean weight. We can make up a few conclusions about health with this information." 
    teacher "But remember, just like BMI, body fat percentage is only one part of the picture." 
    teacher "Health is about balance, and no single number defines a person's well-being."
    "She glances at the clock before wrapping up." 
    image stage_8_event_23 = "/teacher/events/stage8/23.webp"
    scene stage_8_event_23
    teacher "The takeaway? BMI and body fat percentage both help assess health, but they serve different purposes." 
    teacher "BMI is a quick screening tool, while body fat percentage gives us more detail about body composition. Any questions?"
    $ renpy.notify("Body fat percentage unlocked in stat screen.")
    $ teaching_bodyfat_check = 1
    return