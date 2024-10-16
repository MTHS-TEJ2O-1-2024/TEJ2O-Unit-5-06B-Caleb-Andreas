/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Caleb Andreas
 * Created on: Oct 2024
 * This program measures distance with a HC-SR04 5v distance sensor.
*/

// Variables.
let distanceToObject:number = 0

// Happy face at start
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// Find distance on A button pressed.
input.onButtonPressed(Button.A, function() {
    basic.clearScreen()
    distanceToObject = sonar.ping(
        DigitalPin.P1,
        DigitalPin.P2,
        PingUnit.Centimeters
    )
    basic.showNumber(distanceToObject)
    basic.pause(1000)
    basic.showIcon(IconNames.Happy)
})
