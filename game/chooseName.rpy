label chooseName:
    $ name = renpy.input("What is your name?", default = "John").strip()

    if name == "":
        "Please pick an actual name"
        jump chooseName