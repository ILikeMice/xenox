---
title: "Xenox"
author: "@ILikeMice"
description: "An AI Powered robotic arm assistant!"
created_at: "2025-05-21"
---

# Total Time Spent: ~15.5h

# May 22nd

## Start!

Got approval from alex yesterday and wrote down the BOM inso a csv today, also set up my repository with the journal and Readme and stuff, made a rough sketch for the first part(s) in class today :3 Design will definetly vary though, e.g ill add 6 screws and not 4 most likely

### Sketch:

![First sketch](https://github.com/ILikeMice/xenox/blob/main/photos/22-05-1.jpeg?raw=true)

**Session Time Spent: ~1h30mins**

## Basic structure design

Spent a bunch of time in fusion trying to figure out little details but ended up with a design for the component enclosure that im pretty happy with, attached below, making the screw holes next to the block (supposed to be the PSU) align with the edge of the psu so i can actually take it out was pretty painful, gonna have a hole there and thinking about maybe? adding rails to be able to kinda slide everything out for maintenance.

Also got info on what fuse i need for the psu iec socket (confusing but shoutout @Volkov08 for helping)

![First Design](https://github.com/ILikeMice/xenox/blob/main/photos/22-05-2.png?raw=true)

**Session Time Spent: 2h**

# May 23rd

## Getting first Electronics stuff down

So, today I wanted to review my stuff with steppers and so on and realized i might not have enough GPIO pins for all 6 stepper drivers + fan, lights,microphone, speaker, etc., after going on a journey looking up all the stuff i could do i decided to go for a PCF8575 i2c expansion module to control the steppers, turns out i2c is really cool for this. Found it and some basic components ill be needing on aliexpress, and pained myself with installing fritzing thrice with a bunch of problems for about an hour, got a pretty decent schematic down (not without going though a questionable amount of datasheets and manuals) though, attached below:

![First Schematic](https://github.com/ILikeMice/xenox/blob/main/photos/23-05-1.png?raw=true)

**Session Time Spent: 3.5h**

## Trying Kicad!

Decided to try and set up kicad to make a custom PCB for the project, fiddled around with it for a while, but i think it might be overkill for now so ill stick with the fritzing schematic, made more progress on the CAD design of the base (added the thrust bearing slot (kinda??) and made a slot for removing/inserting the PSU)

![Schematic in Kicad](https://github.com/ILikeMice/xenox/blob/main/photos/23-05-2.png?raw=true)

![CAD Design](https://github.com/ILikeMice/xenox/blob/main/photos/23-05-3.png?raw=true)

**Session Time Spent: 2h**

# May 24th

## Continuing CAD Design

I might be rushing the electronics a bit without knowing how much space exactly id have to work with, so i think this should be the approximate design of the base for now, pic 1 is fully assembled with the PSU and the pi (no idea what height so i guesstimated ~1.9cm) in silver and green and the thrust bearing in silver, second pic is the thing on which the bearing will be resting. Decided to make it seperate to the base to minimize supports and quick changes to the design if needed. Also make a holder for the Axis 1 stepper which will need some M3 screws and Bolts, gonna add them to my cart today 

Note: gonna update the BOM soon enough

![Base (Assembled)](https://github.com/ILikeMice/xenox/blob/main/photos/24-05-1.png?raw=true)
![Bearing Rest](https://github.com/ILikeMice/xenox/blob/main/photos/24-05-2.png?raw=true)

**Session Time Spent: 2.5h**

## PCB!

Now that i had the rough amount of space down, i decided to make a pcb so that all the drivers and such arent just loose over the place. This was my first pcb design ever btw so pls dont judge the schematic quality T.T, for some reason i decided to make it in fusion and not in fritzing or kicad (no idea why, maybe bc i wanted the 3d model, i think kicad has that too tho), but i think it turned out decently, i did have a bunch of trouble with finding the sizings of the drivers and the i2c module as i was getting the tmc chip and not the whole module. After literal hours of research i turned to frizing (only place that had the footprint of the tmc2209 and i2c module) and found out theres a ruler function with which i got the thing in about 10mins😭, attached pics below of the pcb, shcematic and pcb inside the base

Also, this might get pretty warm so im thinking of adding a fan for cooling all that somewhere (sides/(front/back) of the psu?)

![PCB inside Base](https://github.com/ILikeMice/xenox/blob/main/photos/24-05-3.png?raw=true)
![Schematic](https://github.com/ILikeMice/xenox/blob/main/photos/24-05-4.png?raw=true)
![PCB](https://github.com/ILikeMice/xenox/blob/main/photos/24-05-5.png?raw=true)

**Session Time Spent: 4h**