# The Owl

![the owl](images/owl_cover.jpg)

The Owl is a 36-key (diodeless!), MX-spaced, wireless keyboard.

It was forked from the [rae-dux](https://github.com/andrewjrae/rae-dux) (itself inspired by the [Architeuthis Dux](https://github.com/tapioki/cephalopoda/tree/main/Architeuthis%20dux) ).

The main difference with the rae-dux is that MX-spacing is used for the keys. This keyboard is also designed with top and bottom plates, so as to protect the MCU and the battery. The mounting holes will fit m3 screws / standoffs.

**Note**: the top-plate doesn't need the mounting holes, so you could remove them from the kicad files.

## Art

The art for the keyboard is from vecteezy.com:
 - top was adapted from https://www.vecteezy.com/vector-art/2531138-black-and-white-line-art-of-owl
 - bottom was adapted from https://www.vecteezy.com/vector-art/3378572-barn-owl-flying-over-black-background

## Firmware

Since the keyboard is the same as the rae-dux, you can use the rae-dux firmware for it, see the [rae-dux ZMK shield](https://github.com/andrewjrae/zmk-config/tree/development/config/boards/shields/rae_dux).

## Build Guide

Checkout the build-guide for the [rae-dux](https://www.tzcl.me/blog/rae-dux). The main difference is that the MCUs are mounted on the bottom of the PCBs.

A small thing you can change is also to put power switche on different sides of the pcb, so that both are in the same position for on-off.

## Important Notes
- **Wireless only**, the 36-key diodeless approach uses the P0 pin which is usually dedicated to TRRS
- There is only one MCU footprint, so **one controller has to be flipped**
- If you want to skip out on the switch, there is no jumper to use the JST
  connector, so you'll have to bodge a wire somewhere, or try shorting the
  switch footprint.
