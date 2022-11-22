#! /usr/bin/env python
"""
This script is used to generate top and bottom plate from a pcb.
The plates will have the same shape than the PCB, only
- switch footprints are replaced by cutouts footprints for the top plate
- mounting pads footprints are kept
- all other footprints are removed, as well as traces
"""

import argparse
from pathlib import Path
from kiutils.board import Board
from kiutils.footprint import Footprint, Position


def get_ref(f: Footprint):
    refs = [i.text for i in f.graphicItems if getattr(i, "type", None) == "reference"]
    assert len(refs) == 1
    return refs[0]


def silks_from_footprint_filename(footprint_filename):
    silk_footprint_1 = Footprint.from_file(footprint_filename)
    silk_footprint_1.layer = "F.Silkscreen"
    silk_footprint_1.position = Position(X=0, Y=0, angle=0)
    silk_footprint_2 = Footprint.from_file(footprint_filename)
    silk_footprint_2.layer = "B.Silkscreen"
    silk_footprint_2.position = Position(X=0, Y=0, angle=0)
    return [silk_footprint_1, silk_footprint_2]


def generate_top_plate(folder, pcb_filename, silk_filename):
    board = Board.from_file(folder / pcb_filename)

    board.traceItems = []
    board.zones = []
    def keep_mx(mx: Footprint):
        ref = get_ref(mx)
        ref_int = int(ref[1:])
        return ref_int % 2 == 0

    pads = [
        f for f in board.footprints
        if f.libraryLink == "SMDPad"
    ]
    switches_distinct = [
        f for f in board.footprints
        if f.libraryLink == "MX" and keep_mx(f)
    ]

    def make_cut_footprint(f: Footprint):
        res = Footprint.from_file("footprints/switch_cut.kicad_mod")
        res.position = f.position
        return res


    board.footprints = pads + [make_cut_footprint(f) for f in switches_distinct]
    if silk_filename:
         board.footprints += silks_from_footprint_filename(silk_filename)

    board.to_file(folder / pcb_filename.replace(".kicad_pcb", "_top_plate.kicad_pcb"))


def generate_bottom_plate(folder, pcb_filename, silk_filename):
    board = Board.from_file(folder / pcb_filename)

    board.traceItems = []
    board.zones = []
    pads = [
        f for f in board.footprints
        if f.libraryLink == "SMDPad"
    ]
    board.footprints = pads

    if silk_filename:
         board.footprints += silks_from_footprint_filename(silk_filename)
    board.to_file(folder / pcb_filename.replace(".kicad_pcb", "_bottom_plate.kicad_pcb"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("--top-silk")
    parser.add_argument("--bottom-silk")
    args = parser.parse_args()
    source = Path(args.source)

    generate_top_plate(source.parent, source.name, args.top_silk)
    generate_bottom_plate(source.parent, source.name, args.bottom_silk)
