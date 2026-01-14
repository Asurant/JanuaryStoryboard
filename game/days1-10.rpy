label day1:
    "You watch the clock strike 12:00. It’s a new year. A new day. A new leaf."
    "You look at your report card from the last semester"
    "It’s a page filled with Fs"
    "With the college application season coming up soon you feel like you should improve those grades."
    "Who knows. Maybe you will be able to get accepted into your dream college. MIT."
    "A sudden wave of tiredness hits you"

    menu:
        "What will you do?"

        "Go to sleep":
            "You fall asleep"
        "Study instead of sleep":
            "After studying for a few hours you feel like you can’t stay awake any longer. You fall asleep."
        "Play video games instead of sleeping":
            "After playing games for a few hours you feel like you can’t stay awake any longer. You fall asleep."
            call game_happy
    jump day2

label day2:
    "Alarm Noises"
    "It’s a new day"

    menu:
        "What will you do?"
        
        "Study":
            #Maybe I can add actual questions here :skull:
            "You study for a few hours"
            call study_gain
        "Play games instead of study":
            "You play video games for a few hours"
            call game_happy
        "Doomscroll intead of studying":
            $ randomValue = renpy.random.randint(1, 2)
            if randomValue == 1:
                "While doomscrolling you see a video posted by one of your classmates in which they got a PS5 for getting all As."
                "You feel like you could do more with your life."
                call doomscroll_happy_loss
            elif randomValue == 2:
                "While doomscrolling you see a funny cat video."
                "You feel happier."
                call doomscroll_happy_gain
    $ randomValue = 0
    "You hear a knock at your door"
    "Hey [name]. Want to play basketball? I just got a new ball for Christmas!"

    menu:
        "Nah I’m good. Not feeling it today":
            barker "Oh… Ok. Maybe tomorrow then?"
        "Sure man. Let’s me go grab my shoes":
            barker "Ok!"
            "You go grab your shoes and play basketball with Barker"
            call outside_happy
            call friendship_gain
        "We always play basketball. Do you want to play video games instead?":
            barker "You know what. Sure. We have played only basketball this break so let's play some."
            "You play Minecraft with Barker for a few hours"
            barker "Yo it’s 6PM. I gotta go now. Bye!"
            call game_happy
            call friendship_gain

    menu:
        "What do you do now?"

        "Study":
            "After studying for a few hours you feel tired. You fall asleep."
            call study_gain
        "Sleep":
            "You sleep"
    
    jump day3

label day3:
    #Add SAT dialogue

    menu:
        "Will you study?"
        "Study":
            "Motivated by your parents, you lock in on your work."
            call study_gain
        "Play games instead of studying":
            $ randomValue = renpy.random.randint(1, 4)
            if randomValue == 1:
                "30 minutes pass. Your mom opens the door."
                mom "What are you doing? Did I not just tell you to study?"
                menu:
                    "I don’t want to study.":
                        mom "It’s only been 30 minutes since you started. I can’t believe you already can’t focus. Get back to studying. The SAT will define your future."
                        call happy_loss
                        call parent_trust_loss
                        "You start studying after a short lecture from your mom."
                        pass
                    "I was studying. I was just taking a short break.":
                        mom "It’s only been 30 minutes since you started. I can’t believe you already can’t focus. Get back to studying. The SAT will define your future."
                        call happy_loss
                        call parent_trust_loss_minor
                        "You start studying after a short lecture from your mom."
            else:
                "You play games for a while. Maybe you should start studying"
                menu:
                    "Study":
                        "Feeling guilty for having not studied earlier. You lock in on your work."
                        call study_gain
                    "Play games instead of studying":
                        $ randomValue = renpy.random.randint(1, 4)
                        if randomValue == 1:
                            "30 minutes pass. Your mom opens the door."
                            mom "What are you doing? Did I not just tell you to study?"
                            menu:
                                "I don’t want to study.":
                                    mom "It’s only been 30 minutes since you started. I can’t believe you already can’t focus. Get back to studying. The SAT will define your future."
                                    call happy_loss
                                    call parent_trust_loss
                                    "You start studying after a short lecture from your mom."
                                    pass
                                "I was studying. I was just taking a short break.":
                                    mom "It’s only been 30 minutes since you started. I can’t believe you already can’t focus. Get back to studying. The SAT will define your future."
                                    call happy_loss
                                    call parent_trust_loss_minor
                                    "You start studying after a short lecture from your mom."
                        else:
                            "You play games for a while."
                            call game_happy       
    jump day4

label day4:
