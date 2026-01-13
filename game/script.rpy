

define player = Character("[name]")
define barker = Character("Barker")
define mom = Character("Mom")

default randomValue = 0

label start:
    call chooseName

    scene bg room

    call day1

    call jobless

    return
