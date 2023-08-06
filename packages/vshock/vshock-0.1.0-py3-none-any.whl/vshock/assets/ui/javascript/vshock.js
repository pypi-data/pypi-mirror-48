class Button {
    constructor(ws, button_number) {
        this.ws = ws
        this.button_number = button_number
    }

    sendValue(value) {
        this.ws.send(JSON.stringify({
            input_type: 1,
            button_number: this.button_number,
            value: value
        }))
    }

    set(value) {
        this.sendValue(value)
    }

    press() {
        this.sendValue(1)
    }

    release() {
        this.sendValue(0)
    }
}

class Axis {
    constructor(ws, button_number) {
        this.ws = ws
        this.button_number = button_number
    }

    sendValue(value) {
        this.ws.send(JSON.stringify({
            input_type: 2,
            button_number: this.button_number,
            value: value
        }))
    }

    incline(value) {
        this.sendValue(value)
    }
}

export const buttonMap = new Map([
    ['select',     0],
    ['leftStick',  1],
    ['rightStick', 2],
    ['start',      3],
    ['up',         4],
    ['right',      5],
    ['down',       6],
    ['left',       7],
    ['l2',         8],
    ['r2',         9],
    ['l1',        10],
    ['r1',        11],
    ['triangle',  12],
    ['circle',    13],
    ['cross',     14],
    ['square',    15],
    ['ps',        16]
])

export const axisMap = new Map([
    ['leftStickY',  0],
    ['leftStickX',  1],
    ['rightStickY', 2],
    ['rightStickX', 3]
])

export default class Controller {
    constructor(ws = new WebSocket('ws://' + location.host + '/input')) {
        this.ws = ws
        for(let [name, number] of buttonMap) {
            this[name] = new Button(this.ws, number)
        }
        for(let [name, number] of axisMap) {
            this[name] = new Axis(this.ws, number)
        }
    }
}
