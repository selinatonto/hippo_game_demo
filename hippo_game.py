print(r'''
                     .^.,*.
                    (   )  )
                   .~       "-._   _.-'-*'-*'-*'-*'-'-.--._
                 /'             `"'                        `.
               _/'                                           `.
          __,""                                                ).--.
       .-'       `._.'                                          .--.\
      '                                                         )   \`:
     ;                                                          ;    "
    :                                                           )
    | 8                                                        ;
     =                  )                                     .
      \                .                                    .'
       `.            ~  \                                .-'
         `-._ _ _ . '    `.          ._        _        |
                           |        /  `"-*--*' |       |  mb
                           |        |           |       :
 ~~~~~~~---   ~-~-~-~   -~-~-~-~-~-~~~~~~  ~~~~  ~-~-~-~-~-~-~-
------~~~~~~~~~----------~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
 ~~~~~~~~~   ~~~~~~~~~       ~~~~~~~   ~~~~~~~~~  ~~~~~~~~~~~~~~~''')

print("Welcome to HippoWorld!")
hippo = input("This is Hippo adventure, which direction will you like to go? left or right?\n").lower()

if hippo == "right":
    print("Welcome to the Hippo bridge where you can cross to meet other hippos!")
    next_step = input("Will you cross or turn back?\n").lower()
    if next_step == "turn back":
        print("You got captured by the wolves. Game over!")
    elif next_step == "cross":
        second_step = input("You just arrived at the gate of the hippo festival! Will you knock or climb?\n").lower()
        if second_step == "climb":
            print("You just got arrested by the hippo police!")
        elif second_step == "knock":
            print("Hurray you just arrived at the hippo festival!!!")
else:
    print("Oops you fell in the lion den. Game over!")


