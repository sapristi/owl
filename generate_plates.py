#! /usr/bin/env python
import argparse
from pathlib import Path
from kiutils.board import Board
from kiutils.footprint import Footprint


def get_ref(f: Footprint):
    refs = [i.text for i in f.graphicItems if getattr(i, "type", None) == "reference"]
    assert len(refs) == 1
    return refs[0]



def generate_top_plate(folder, pcb_filename):
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

    board.to_file(folder / pcb_filename.replace(".kicad_pcb", "_top_plate.kicad_pcb"))


def generate_bottom_plate(folder, pcb_filename):
    board = Board.from_file(folder / pcb_filename)

    board.traceItems = []
    board.zones = []
    pads = [
        f for f in board.footprints
        if f.libraryLink == "SMDPad"
    ]
    board.footprints = pads
    board.to_file(folder / pcb_filename.replace(".kicad_pcb", "_bottom_plate.kicad_pcb"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    args = parser.parse_args()
    source = Path(args.source)

    generate_top_plate(source.parent, source.name)
    generate_bottom_plate(source.parent, source.name)
