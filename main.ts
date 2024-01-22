function ShowTextList (list: any[]) {
    for (let value of list) {
        basic.clearScreen()
        basic.showString("" + (value))
        basic.pause(500)
    }
}
input.onButtonPressed(Button.A, function () {
    basic.showNumber(textlist1.length)
    ShowTextList(textlist1)
    basic.pause(500)
    textlist1.shift()
    ShowTextList(textlist1)
    basic.pause(500)
    textlist1.pop()
    ShowTextList(textlist1)
    basic.pause(500)
    textlist1.insertAt(0, char)
    ShowTextList(textlist1)
})
let char = ""
let textlist1: string[] = []
textlist1 = [
"a",
"b",
"c",
"d"
]
char = "X"
