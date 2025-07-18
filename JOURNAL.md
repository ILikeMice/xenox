---
title: "Xenox"
author: "@ILikeMice"
description: "An AI Powered robotic arm assistant!"
created_at: "2025-05-21"
---

# Total Time Spent: ~58.5h

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


# May 25th

## Joints 1 & 2!

Made a bunch of cad progress today! First, I made a round shape thing for the 1st joint that would also hold the second joint in the middle: 
![Joints v1](https://github.com/ILikeMice/xenox/blob/main/photos/25-05-1.png?raw=true)

This turned out to be really impractical though because id need to magically insert a rod through the 2nd joint's arm part and then somehow also fit the servo next to it, so i decided to scrap that design and make a flat spinning base with a couple holders for the 2nd joint: 

![Finished-ish thing cross-section](https://github.com/ILikeMice/xenox/blob/main/photos/25-05-2.png?raw=true)

for this ill need some gears, a rod and bearings (i already have the bearings at home), which added up to ~10-15$. I think its worth it tho since its 5 pcs of each so ill be able to reuse that for future joints. I also added some heat inserts for attaching the servos and future stuff with screws instead of glue, and some cable sleeving for the cables. I should really update my BOM soon

Speaking of cables, my next step might be making holes for the cables to pass through, i think itll be quite a challenge tho since i cant really fit a slip ring into the first joint, so ill have to account for spinning for the first 2 servos, I think ill try to add a slip ring at the next joint though.

Also, thinking about joint 3, I might remodel joint 2 to just use 2 bearings without a rod for that so i can fit a stepper directly in the center of it without the rod interfering (totally not copied from a guy i found online :3)

Design today:

![Design 25-05](https://github.com/ILikeMice/xenox/blob/main/photos/25-05-3.png?raw=true)


**Session Time Spent: ~6h**


# June 3rd

## A bit of redesign and joint 3!

I havent posted in a couple of days, so ill summarize the progress as one session here. 

First of all, i changed the overall look of the "first" arm part, mainly so that joint 3 is a circle and can freely rotated instead of bein rectangular-ish and me having to put a stepper at the top. I also removed the need for a rod in the middle and made the whole thing be held in place by 2 bearings on each side. I then made a little hole and sliced the thing in two so i could add the 3rd stepper right inside of the arm. I think this should remove the need for screws there, but i might try adding slots for heat inserts somehow.

I also moved the whole gear thing to the outside of the 2 holders that hold the arm and made a decent holder for the stepper that ill also hold with some screws (should hopefully be able to hold, i gotta do that for the arm holders too). Speaking of the gear thing, ill most likely 3d print the bigger gear, which allows enough budget to maybe get a finer nozzle for better precision on that, since afaik 3d printed gears need some more precision to work decently (it should also save me some budget when i need more gears in the future), and with it being 3d printed ill be able to fit some heat inserts in there to attach it to the arm piece directly without a rod 

Some pictures:

![Cross-section](https://github.com/ILikeMice/xenox/blob/main/photos/03-06-1.png?raw=true)

![Overall design](https://github.com/ILikeMice/xenox/blob/main/photos/03-06-2.png?raw=true)

I also made a rod with some slots for heat inserts for the 3rd joint which ill somehow attach to the next joint later on, plus i started making the heat insert radius use a variable so i wont have to change all of the holes if i ever change my mind on something



**Total time spent across sessions: ~10.5h?** 

## BOM update!!

Finally got to updating the BOM, i think that should be pretty much all for now, added some cables, heat inserts, flange couplings, etc. check ./BOM.csv or ./README.md for more details!

**Total session time spent: ~30mins**

# June 12th


## Redesign of joint 3 and 2

I realized that im kinda dumb and accidentially made joint 3 fully wrong (view photo below)


![alt text](https://github.com/ILikeMice/xenox/blob/main/photos/12-06-3.png?raw=true)

As you can see, the U axis is supposed to move the arm down, whereas i made it rotate the arm. I dont really want it that way so i redesigned the joint.


![alt text](https://github.com/ILikeMice/xenox/blob/main/photos/12-06-1.png?raw=true)

I put the stepper into the end of the joint, but doing a bunch of research (also considered high torque servos but meh, might look into them more though), the steppers im using right now will probably not serve close to enough torque, so i will probably redesign this to use gears.

Speaking of not enough torque, i decided to go with a stronger motor for joint 2 since it has to carry whe whole arm. I also upped the gear ratio from 3:1 to 5:1 and changed the mount. I found another stepper motor after designing this which isnt aliexpress choice so i gotta pay for shipping, it does however give me 40Ncm torque instead of 25Ncm on the choice stepper, so i might change this too.

Assuming i use the 25Ncm stepper, ill get 125N of force at joint 2, which gives me about 4N torque @ 30cm and 2N @ 60cm.
With the 40Ncm stepper ill get 6N @ 30cm and 3N @ 60cm.

I should look into nema23 steppers.

Also, after looking at my torque amounts, i might cut the max range of the arm to 60cm instead of 1m.

Current Joint 2 mount: 

![mount](https://github.com/ILikeMice/xenox/blob/main/photos/12-06-2.png?raw=true)

**Total time spent: ~ 5h**


# June 13th

## Work on Joint 3!

So, i did a bunch of research on aliexpress and watched a ton of youtubers making hobbyist arms, and decided to keep a stronger motor for joint 2 only, since thats carrying the whole weight of the arm. I didnt want to use multiple since i got some limited amount of space in the base of the arm and my current small drivers cant handle the current needed for stronger motors.

Inspired by Steward Technologies on youtube, i decided to use the ton of space i had inside the arm to make a gear setup for joint 3.

![alt text](https://github.com/ILikeMice/xenox/blob/main/photos/13-06-1.png?raw=true)

This turns the 13Ncm torque from the small stepper into 208Ncm with a total gear ratio of 16:1. I still have to redesign the joint itself at the top to have a gear in the middle with 2 holders on the outside (opposite of the current setup)

I also found out from another youtuber that im absolutely stupid and my custom pcb is totally useless since i can get RAMPS 1.4 board for a fraction of the price on aliexpress. Its got everything except i2c, but i dont mind a bit of cabling between the board and the i2c module.


**Session time spent: ~3.5h** (didnt track on this session, guesstimated)


## July 3rd

Had some time to work on the project in the last weeks, didnt write journal logs though since i was adding 1 mini feature per session but that kinda built up over some time.

Current build:

![alt text](image.png)
![alt text](image-1.png)

So, i started and kinda made joint 4 after quite a couple redesigns, the gear being in the middle was pretty annoying since id have to kinda print it in multiple parts and the cylinder of the arm would probably be weirdly attached to the whole structure. In the end i decided to move it to the side, but in exchange i had to make the last gear a bit long (actually writing this i realize i could be 2/3 as long idk why i did all that).

I also designed the cover of joint 3 to be attachable with a couple screws (4 screws to assemble it, 8 to attach to the big cylinder (on which i still gotta see how i wanna assemble it))

Also dug around quite a bit in search of better steppers, couldnt find anything better than what i currently have though.

Plans for the last 2 joints (the "hand part") are to probably use some lightweight steppers since it doesnt need that much torque to hold stuff and using steppers would make it real hard on joints 2 and 3. Also, depending on the steppers ill probably be able to get away with a 15A PSU which would actually fit inside the housing for the arm as planned.

I additionally gotta get inspired by something to get a decent gripper down and find a place to install the microphone and speaker.


**Total Time Spent over Sessions: around 12h**


## July 11th

Made progress on joint 5 and started working on the gripper, thinking of how to make the hand part modular (will be one of the last things after the gripper)

### Joint 5

![alt text](image-2.png)

Thought a design like this would look the best overall, the only downside of it being the possibility of the joint breaking off. I still need to see how id fix that :/, Joint 4 is fully finished though, with an added bearing for stability of the rod.

To rotate Joint 5 I decided on a MG90S servo, its got metal gears, a 270deg range and pretty decent torque. I will also be using one for joint 6, but for the gripper ill use a continuous rotation servo i got laying around.

Speaking of the gripper:

![alt text](image-3.png)

this is the coolest mechanism i found (also basically the only one with 3 fingers which could also possibly fit the camera in the middle), however, the cad files for it arent available so i had to make a couple prototypes to get to this design:

![alt text](image-4.png)


its just an outline of the gripper to see how the mechanism would perform when printed, which wasnt with much success sadly. Main problems are the gears changing a bit due to their size and my .4mm nozzle (even after i changed the outer gears to this "inverted" type), which shouldnt be a problem with a .2 nozzle though, and the outer gears not touching the middle worm gear. To fix that though, i plan on adding a couple springs and make the gear holders rotateable, so the gears are always pushed against the middle gear. Printing the worm gear is also pretty hard, ill look into buying one.

**Session time spent: ~6h**