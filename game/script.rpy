

define player = Character("[name]")
define barker = Character("Barker")
define mom = Character("Mom")

default randomValue = 0
default intelligence = 0
default happiness = 50
default friendship = 50
default money = 0
default grade = 30
default parent_trust = 70
default teacher_trust = 50

label start:
    call chooseName

    scene bg room

    call day1

    call jobless

    return

label study_gain:
    $intelligence+= 1
    call happy_loss
    return

label outside_happy:
    $happiness+= 1
    return

label game_happy:
    $happiness+= 1
    return

label happy_loss:
    $happiness-= 1
    return

label doomscroll_happy_loss:
    $happiness-= 1
    return

label doomscroll_happy_gain:
    $happiness+= 1
    return

label friendship_gain:
    $friendship+= 1
    return

label minimum_wage:
    $money += 13
    return

label parent_trust_loss:
    $parent_trust-=10
    return

label parent_trust_loss_minor:
    $parent_trust-=5
    return

label parent_trust_gain:
    $parent_trust+=5
    return

label teacher_trust_loss:
    $parent_trust-=5
    return

label teacher_trust_gain:
    $parent_trust+=5
    return

