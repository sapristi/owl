# The Owl


The Owl is a 36-key (diodeless!), wireless keyboard, forked from the [rae-dux](https://github.com/andrewjrae/rae-dux) (itself inspired by the [https://github.com/tapioki/cephalopoda/tree/main/Architeuthis%20dux](Architeuthis Dux)).
I mostly changed the outer form of the keyboard, and added m3 holes so that it can be built with the associated added front and bottom plates.

*This has now been printed and is working perfectly with ZMK!*
The ZMK shield can be found [https://github.com/andrewjrae/zmk-config/tree/development/config/boards/shields/rae_dux](here), as far as I can tell small custom projects
like this aren't to be merged into ZMK main, so you'll have to emulate what  my [`zmk-config`](https://github.com/andrewjrae/zmk-config/tree/development/config).

## Build Guide
The wonderful @tzcl created a [https://www.tzcl.me/blog/rae-dux](build guide) for the rae-dux, so if you are curious about building the board, but don't have experience with this sort of thing go check it out!

## Important Notes
- **Wireless only**, the 36-key diodeless approach uses the P0 pin which is usually dedicated to TRRS
- There is only one MCU footprint, so **one controller has to be flipped**
- If you want to skip out on the switch, there is no jumper to use the JST
  connector, so you'll have to bodge a wire somewhere, or try shorting the
  switch footprint.
- Kicad files are 6.0, so unfortunately not backwards compatible.
