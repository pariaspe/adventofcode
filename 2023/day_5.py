"""
Day 5 | Advent of Code 2023
"""

from dataclasses import dataclass, field


@dataclass
class AlmanacMap:
    """ Almanac Map """
    source: list[int] = field(default_factory=list)
    destination: list[int] = field(default_factory=list)
    range_length: list[int] = field(default_factory=list)

    def source_to_destination(self, source: int) -> int:
        """Get destination from source"""
        for i, source_range in enumerate(self.source):
            if source in range(source_range, source_range + self.range_length[i]):
                return self.destination[i] + (source - source_range)
        # Not mapped --> destination = source
        return source

    def append_line(self, line: str):
        """Append map to AlmanacMap"""
        destination, source, range_length = line.split(' ')
        self.source.append(int(source))
        self.destination.append(int(destination))
        self.range_length.append(int(range_length))


@dataclass
class Almanac:
    """ Island Island Almanac """
    seeds: list[int] = field(default_factory=list)
    maps: dict[str, AlmanacMap] = field(default_factory=dict)

    @staticmethod
    def from_file(filename: str) -> 'Almanac':
        """Create Almanac from file"""
        almanac = Almanac()
        current_map = ''
        with open(filename, encoding='utf-8') as f:
            for line in f.readlines():
                if not line.strip():
                    continue

                if line.startswith('seeds'):
                    _, seeds = line.strip().split(':')
                    for seed in seeds.strip().split(' '):
                        almanac.seeds.append(int(seed))
                    continue

                if 'map' in line:
                    current_map, *_ = line.strip().split(' ')
                    almanac.maps[current_map] = AlmanacMap()
                    continue

                almanac.maps[current_map].append_line(line.strip())
        return almanac

    def get_map_from_source(self, source: str) -> str:
        """Get map from source"""
        for map_key in self.maps:
            if source in map_key:
                return map_key
        return ''


def part_one(filename: str) -> int:
    """Solution for part one"""
    almanac = Almanac.from_file(filename)
    source = 'seed'
    seeds = almanac.seeds
    while True:
        mapping = almanac.get_map_from_source(source + '-to')
        if not mapping:
            break
        source, _, destination = mapping.split('-')

        new_seeds = []
        for seed in seeds:
            new_seeds.append(almanac.maps[mapping].source_to_destination(seed))
        seeds = new_seeds

        source = destination
    return min(seeds)


def part_two(filename: str) -> int:
    """Solution for part two"""
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            if not line.strip():
                break

    return 0


if __name__ == "__main__":
    assert part_one("5-test.txt") == 35
    solution_part_one = part_one("5-input.txt")
    print(f"{solution_part_one=}")

    # assert part_two("5-test.txt") == 30
    # solution_part_two = part_two("5-input.txt")
    # print(f"{solution_part_two=}")
