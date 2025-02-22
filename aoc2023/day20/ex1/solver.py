import sys
import re
from dataclasses import dataclass, field
from collections import namedtuple
from enum import Enum
from queue import Queue
from abc import ABC, abstractmethod

import pydot


class Pulse(Enum):
    LOW = 0
    HIGH = 1

@dataclass
class Module(ABC):
    slug: str
    output: list["Module"] = field(default_factory=list)
    input: list["Module"] = field(default_factory=list)

    @abstractmethod
    def pulse_handler(self, pulse: Pulse, src: "Module") -> Pulse | None:
        pass

@dataclass
class FlipFlop(Module):
    is_on: bool = False

    def pulse_handler(self, pulse: Pulse, src: "Module") -> Pulse | None:
        if pulse == Pulse.HIGH:
            return None

        if self.is_on:
            to_send = Pulse.LOW
        else:
            to_send = Pulse.HIGH

        self.is_on = not self.is_on
        return to_send

@dataclass
class Base(Module):
    # Do nothing
    def pulse_handler(self, pulse: Pulse, src: "Module") -> Pulse | None:
        return None

@dataclass
class Conjunction(Module):
    input_modules_state: dict[str, Pulse] = field(default_factory=dict)

    def init_state(self):
        for module in self.input:
            self.input_modules_state[module.slug] = Pulse.LOW


    def pulse_handler(self, pulse: Pulse, src: "Module") -> Pulse | None:
        self.input_modules_state[src.slug] = pulse

        for pulse in self.input_modules_state.values():
            if pulse == Pulse.LOW:
                return Pulse.HIGH

        return Pulse.LOW


class Broadcaster(Module):

    def __init__(self, *args, **kwargs):
        super().__init__("broadcaster", *args, **kwargs)

    def pulse_handler(self, pulse: Pulse, src: "Module") -> Pulse | None:
        return pulse


WiredPulse = namedtuple("WiredPulse", ["src", "dst", "pulse"])

def print_modules(modules: dict[str,  Module]) -> None:
    graph = pydot.Dot("my_graph", graph_type="digraph")
    seen = set()

    def print_module_rec(module: Module) -> None:
        if module.slug in seen:
            return

        seen.add(module.slug)
        graph.add_node(pydot.Node(module.slug))

        for output in module.output:
            graph.add_edge(pydot.Edge(module.slug, output.slug))
            print_module_rec(output)

    print_module_rec(modules["broadcaster"])
    graph.write("output.png", format="png")

def parse_input(input_file: str) -> dict[str, Module]:
    modules = {}

    def create_module(module_type: str, slug: str) -> Module:
        match module_type:
            case "":
                return Broadcaster()
            case "%":
                return FlipFlop(slug)
            case "&":
                return Conjunction(slug)
            case "base":
                return Base(slug)

    with open(input_file) as f:
        configuration_m = []

        for line in f.readlines():
            configuration_m.append(re.match(r"([%&]?)([a-z]+) -> ([a-z, ]+)", line.strip()))

        # Init modules
        for m in configuration_m:
            if m.group(2) not in modules:
                modules[m.group(2)] = create_module(m.group(1), m.group(2))

        # Add links between modules
        for m in configuration_m:
            for dest in m.group(3).split(","):
                dest = dest.strip()

                # Edge case to handle output module which is not really a module ...
                if dest not in modules:
                    modules[dest] = create_module("base", dest)

                modules[m.group(2)].output.append(modules[dest])
                modules[dest].input.append(modules[m.group(2)])

        # Init state for Conjunction modules
        for module in modules.values():
            if type(module) is Conjunction:
                module.init_state()

    return modules


def main(input_file: str) -> int:
    """
    https://adventofcode.com/2023/day/X#part1
    """
    modules = parse_input(input_file)
    print_modules(modules)

    wired_pulses = Queue()
    low_pulse_nb, high_pulse_nb = 0, 0

    for _ in range(1000):
        wired_pulses.put(WiredPulse(None, modules["broadcaster"], Pulse.LOW))

        while not wired_pulses.empty():
            wp = wired_pulses.get()
            if wp.pulse == Pulse.HIGH:
                high_pulse_nb += 1
            elif wp.pulse == Pulse.LOW:
                low_pulse_nb += 1
            #print(f"[{wp.src.slug if wp.src else 'button'}] === {wp.pulse} ==> [{wp.dst.slug}]")

            pulse_response = wp.dst.pulse_handler(wp.pulse, wp.src)
            if not pulse_response:
                continue
            for dst in wp.dst.output:
                wired_pulses.put(WiredPulse(wp.dst, dst, pulse_response))

    return low_pulse_nb * high_pulse_nb


if __name__ == "__main__":  # pragma: no cover
    if len(sys.argv) != 2:
        raise ValueError(f"Invalid parameter, usage : {sys.argv[0]} <input_file.txt>")
    print(main(sys.argv[1]))
