def ShowTextList(list2: List[any]):
    for value in list2:
        basic.clear_screen()
        basic.show_string("" + str((value)))
        basic.pause(500)

def on_button_pressed_a():
    basic.show_number(len(textlist1))
    ShowTextList(textlist1)
    basic.pause(500)
    textlist1.shift()
    ShowTextList(textlist1)
    basic.pause(500)
    textlist1.pop()
    ShowTextList(textlist1)
    basic.pause(500)
    textlist1.insert_at(0, char)
    ShowTextList(textlist1)
input.on_button_pressed(Button.A, on_button_pressed_a)

char = ""
textlist1: List[str] = []
textlist1 = ["a", "b", "c", "d"]
char = "X"