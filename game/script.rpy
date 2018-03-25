# The script of the game goes in this file.

# my images
image blackBG = "#000"
image classBG = "BG/800x600BGclass.png"
image botImage default = "bot/bot_default.png"
image Sofia default = "Sofia/Sofia_default.png"
image Milan default = "Milan/Milan_default.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define M1 = Character("TOAMMY")
define M2 = Character("Michael")
define F1 = Character("Milan", image='Milan')
define F2 = Character("Sofia", image='Sofia')
define T1 = Character("Mrs. Crawley")
define bot = Character("COLE", image='botImage')
define cat = Character("Cat")
define PC = Character("Me") #Uhh, we can add functionality to change names later



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room
    scene blackBG

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    "Today is a special day, as I start my second year at the new school, DeWitt High!" 
    "The city recently built this new facility last year and I was signed up as one of the first new students."
    
    # first option
    menu:
        "I\'m sad to leave my old school...":
            jump choice1_sad
        
        "I\'m glad I left my last school.":
            jump choice1_glad

    label choice1_sad:

        #$ menu_flag = True

        "All of my friends from my old school stayed behind, but my mom signed me up for this new school." 
        "She said the facilities were cutting edge so she wanted me to have the best high school experience possible." 
        "... I guess she wasn’t talking about my social life."
        
        jump choice1_done

    label choice1_glad:

        #$ menu_flag = False # these menu flags are for later, for when we figure out
        # what this choice affects.

        "My old school was pretty terrible. I hated the kids, I hated the teachers." 
        "The facilities were old and grimy. All the materials is centuries old, and they haven’t updated the school in a while." 
        "I asked my mom to transfer me here as soon as I was aware that this facility would be built. I was accepted and I’m now headed off to the better facilities that DeWitt High has to offer."
       
        jump choice1_done

    label choice1_done:

    # choice 1 done
    "Regardless of how I feel, this represents a fresh, new start. One that I will go through, one way or another." 
    "This school seems to be pretty free in terms of structure." 
    "I can take any classes when they’re available, but I need to take at least four classes that fall under my concentration. Of course I can sit in some other classes, but it wouldn’t count towards the four that I’m required to take." 
    "Each day is separated into 6 blocks of time, so if I want, I can take two extra classes a day or just take no classes for the two extra blocks to either study or just hang out." 
    "For the first day, however, I must take this introductory class first thing in the morning."
    
    #maybe a different scene?
    scene classBG
    
    #calling roll
    "When I arrived, not many students were there. Around The teacher walked in and introduced herself as Mrs. Crawley. About 15 minutes into class, she started to call role." 
    "The teacher called out names, but she seemed to miss my name."
    
    T1 "Did I miss anyone?"
    PC "You didn\'t call my name!"
    T1 "What\'s your name?"
    
    # pick your name and gender HAVE TO ADD GENDER FUNCTIONALITY
    $ nameChosen = False
    #$ count = 0
    python:
        while (nameChosen == False):
            name = renpy.input("What\'s your name?")
            
            name = name.strip()
            nameChosen = True
            if not name:
                nameChosen = False
                #call expression "noName" pass (count)
            #count += 1
    
    #label noName (count=1):
     #   $ T1("Uhh... Hello?")
        
    #label noName (count=2):
     #   $ T1("I do need your name...?")
        
    #label noName (count=3):
     #   $ T1("Please give me your name.")
        
    #label noName (count=4):
     #   $ T1("Uhh... OK, I can see that you\'re not suited for school...")
      #  $ T1("I think it\'s best you leave.")
       # jump badEnd_noName

    T1 "Oh! I\'m sorry. I seemed to have skipped your name. Alright [name], I\'ve marked you as absent."
    T1 "Haha! I\'m kidding."
    
    T1 "Hello class, and welcome to DeWitt High! Today\'s the only day you\'ll have to take this class as this is pretty much an introductory class to show you the ropes of our school!" 
    T1 "It\'s like homeroom, but it\'s only one day. I hope you enjoy your time here." 
    T1 "Today, you\'ll be given a robotic buddy our school has recently developed to help your development here."
    T1 "We call it the Companion Overseer for Leading Education MK I or COLE for short. Isn’t he the cutest little thing you’ve seen today? Besides me, of course!"
    
    centered "COLE OBTAINED!"
    
    show botImage default
    
    #COLE
    bot "Hello! I am your new COLE unit! Nice to meet you!"
    bot "I will assist you in your courses and daily life! I will learn things by observing you and your surroundings and will adjust to reflect what I think you may need." 
    bot "You may refer back to the notes I’ve recorded over time by pressing on my face. I will also present you with all the courses currently available when the time comes."
    bot "Please feel free to use me as you see fit."
    
    show botImage default at right
    
    T1 "I’ve also given you an example schedule to help you get used to our school structure. You don’t have to stick to this schedule if you don’t want to, but you DO have to meet at least the four class requirement."
    T1 "Failure to do so may result in your expulsion."
    
    centered "SAMPLE SCHEDULE OBTAINED!"
    
    $ classPeriod = 2
    
    menu classOption:
        "Follow the example schedule Mrs. Crawley gave me.":
            jump choice2_Schedule
        
        "I know what I'm doing. I'll deviate from the schedule.":
            jump choice2_noSchedule
        
    label choice2_Schedule:
        $ schedule_choice2Flag = True
        bot "Excellent choice. Following recommendations will ensure that you excel in this academy."
        bot "Your first class will be Chemistry, then Statistics, History of Eugenics, and Biology."
        bot "After that, you'll have an option to pick an elective or go home."
        
        "The robot, COLE, dinged."
        
        bot "Oh! There's 5 minutes left before Chemistry begins. I would hurry if I were you."
        hide botImage default
        
        scene blackBG
        "Thankfully, the class wasn't that far away."
        
        scene classBG
        
        jump chem_class
    
    label choice2_noSchedule:
        $ schedule_choice2Flag = False
        return
    
    #label choice2_end:
    
    label chem_class:
        if classPeriod is 2:
            "I looked around the classroom for an open seat." 
            "There's one next to a fashionable-looking, red-headed girl wearing a light pink blouse, grey scarf and a jean skirt."
            "She looks nice, so I decide to approach."
            
            PC "Hello! Is anyone sitting in this seat?"
            
            show Sofia default
            "The girl grimaced... Well, then!"
            
            F2 "Ehh... maybe not you..."
            "Yikes... Should I sit here anyway? The seats seem to be filling up."
            
            menu Sofia_choice1:
                "Take the seat anyway.":
                    jump Sofia_take
                
                "Try to find another seat.":
                    jump Sofia_no
            
            label Sofia_take:
                F2 "Alright, fine. Do what you want."
                $ Sofia_choice1Flag = True
                jump Sofia_choice1End
            
            label Sofia_no:
                hide Sofia default
                "I looked around the room and didn't find any more open seats."
                "When I turned back, the seat I saw earlier was already taken. Well! Looks like I'm going to stand for this calss..."
                $ Sofia_choice1Flag = False
                jump Sofia_choice1End
            
            label Sofia_choice1End:
                #jump chem_classNormal
                pass
                
        else:
            "I looked around the classroom for an open seat. It was a bit hard to find one, but I found one eventually."
            #jump chem_classNormal
        
        label chem_ClassNormal:
            "Class continued without incident."
            
            if Sofia_choice1Flag is True:
                "After class, Sofia stopped me, looking apologetic."
                F2 "Sorry for being so rude at the beginning of class, it's just..."
                F2 "your outfit looks terrible."
                F2 "Lime green doesn't work on anyone, sweetie, least of all you."
                F2 "The school holds fashion classes throughout the day. You NEED to attend one."
                F2 "Personally, I'm going at the end of the day today. It's my way of therapy after seeing all the horrid outfits throughout the day."
                
                PC "Alright... I might go."
                hide Sofia default
            
            $ classPeriod += 1
            scene blackBG
            "It's time to go to the next class."
            
            if schedule_choice2Flag is True:
                jump stat_class
            
    label stat_class:
        scene classBG
        
        if classPeriod is 3:
            $ period3_flag = True
        else:
            $ period3_flag = False
        
        "Entering the classroom, I saw that there were seats in the front and the back."
        "Where should I sit?"
        
        menu Milan_choice1:
            "I should sit in the front.":
                jump Milan_front
            
            "I should sit in the back.":
                jump Milan_back
        
        label Milan_front:
            if period3_flag is True:
                $ Milan_choice1Flag = True
            
            jump stat_ClassNormal
        
        label Milan_back:
            $ Milan_choice1Flag = False
            
            if period3_flag is True:
                "I walked to the back. It actually seemed colder back here; maybe it's the AC above, or that almost no one was sitting back here."
                "Just as class was about to start, a vaguely dazed-looking girl shuffled into the classroom. Her bag seemed to be bulging with books."
                
                show Milan default
                
                "She seemed like someone who would know statistics. And I'm in luck! She shuffled to the back, and sat right next to me!"
                "Class started, so I acknowledged her and turned my attention to the lecture."
                
                F1 "Umm, excuse me?"
                "She whispered."
                PC "Huh?"
                F1 "Can I read along your statistics book?"
                PC "Uh, sure..."
                
                "Maybe my first impression was off..."
                PC "What happened to your book?"
                F1 "It hasn't arrived yet, although I may've not pressed... the order button... Oh well."
                
                "I pushed my book toward her so that we could reference the examples the teachers went over."
                "Something was bothering me, though..."
                
                PC "Y'know, that's a really full bag you got there. I would've thought you'd have your stat book in there."
                F1 "Hmm? Oh, I like... reading? Like, like..."
                
                "She just... started pulling out her books, one after another. It's just a lot of short novels and novellas."
                "There was one large book in there that she didn't pull out."
                
                PC "What's that one called?"
                F1 "Oh... that's just... my favorite book."
                
                "She pulled out a creepy, leathery book. I have the oddest sensation that the book is watching my every move..."
                "... whispering to me..."
                "She said the name, but I missed it... I couldn't focus until she put it away."
                PC "O-okay..."
                
                jump stat_ClassNormal
                
            else:
                jump stat_ClassNormal
        
        label stat_ClassNormal:
            "Class passed with nothing too strange. I'm a bit more knowledgeable today. Clearly worth the time I spent on it."
            
            if Milan_choice1Flag is True:
                "The only odd thing was a dazed girl shuffling all the way to the back at the beginning of class."
                "Her bag seemed to be bulging with books. Odd."
            elif period3_flag is True:
                "At the end, the girl got my attention"
                F1 "If you're interested in these sorts of books, we have a literature class at the end of the day."
                
                "She smiled a little."
                F1 "I actually brought my favorite book to show the class today. It should be fun. You should come!"
                
                PC "I'll... consider it."
                
            "Now it's time to go to my next class!"
            scene blackBG
                
            $ classPeriod += 1
            
            if schedule_choice2Flag is True:
                jump eug_class
                
    label eug_class:
        scene classBG
    
    label bio_class:
        scene classBG
    
    label home_choice:
        scene classBG
    
    label Mach_sclass:
        scene classBG
    
    label Fash_sclass:
        scene classBG
    
    label PE_sclass:
        scene classBG
    
    label lit_sclass:
        scene classBG
    
    
    label badEnd_noName:
        # add bad ending scene
        return
    # This ends the game.

    return
