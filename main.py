def on_logo_long_pressed():
    onLogoPress()
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def cubePattern():
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . # # # .
                . # . # .
                . # # # .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . # # # .
                . # . # .
                . # # # .
                . . . . .
    """)
    basic.pause(100)
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
    """)
def playMelodies():
    music.play_melody("C C E A F G C C ", 200)
def onLogoPress():
    basic.show_icon(IconNames.CHESSBOARD)

def on_button_pressed_ab():
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

basic.show_string("Sizing Cube")
basic.show_string("Enjoy!")

def on_forever():
    cubePattern()
basic.forever(on_forever)

def on_in_background():
    for index in range(1e+45):
        playMelodies()
control.in_background(on_in_background)
