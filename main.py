def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()
    basic.show_icon(IconNames.SMALL_HEART)
    basic.clear_screen()
    basic.show_icon(IconNames.HEART, 1)
basic.forever(on_forever)
