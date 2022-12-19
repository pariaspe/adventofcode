from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class File:
    name: str
    size: int

    def __str__(self):
        return f"- {self.name} (file, size={self.size})\n"


@dataclass
class Folder:
    name: str
    parent: Folder
    subfolders: dict[str, Folder] = field(default_factory=dict)
    files: list[File] = field(default_factory=list)

    def add_file(self, file: File):
        self.files.append(file)

    def add_folder(self, folder: Folder):
        self.subfolders[folder.name] = folder

    def files_size(self):
        size = 0
        for file in self.files:
            size += file.size
        return size

    def size(self):
        size = self.files_size()
        for folder in self.subfolders.values():
            size += folder.size()
        return size

    def __str__(self):
        output = f"- {self.name} (dir, size={self.size()})\n"
        for file in self.files:
            output += f"    {file}"
        for folder in self.subfolders.values():
            output += f"    {folder}"
        return output


def parse_cmd(cmd: str):
    """returns dir"""
    tokens = cmd.split(" ")
    if tokens[1] == "cd":
        return tokens[2]
    return ""


def parse_output(output: str, current_dir: Folder):
    tokens = output.split(" ")
    if tokens[0] == "dir":
        current_dir.add_folder(Folder(tokens[1], current_dir))
    else:
        current_dir.add_file(File(tokens[1], int(tokens[0])))


def find_folder(root: Folder, max_size: int = 0, min_size: int = 0):
    folders = set()
    if (max_size == 0 or root.size() <= max_size) and \
            (min_size == 0 or root.size() >= min_size):
        folders.add((root.name, root.size()))

    for folder in root.subfolders.values():
        folders = folders.union(find_folder(folder, max_size, min_size))
        if (max_size == 0 or folder.size() <= max_size) and \
                (min_size == 0 or folder.size() >= min_size):
            folders.add((folder.name, folder.size()))
    return folders


def main(filename):
    with open(filename) as f:
        lines = f.readlines()

    root = Folder("/", None)
    lines.pop(0)  # skips '$ cd /'

    current_dir = root
    for line in lines:
        if not line.strip():
            break
        if line.startswith("$"):
            cd_dir = parse_cmd(line.strip())
            if cd_dir:
                if cd_dir == "..":
                    current_dir = current_dir.parent
                    continue
                current_dir = current_dir.subfolders.get(cd_dir)
        else:
            parse_output(line.strip(), current_dir=current_dir)

    light_folders = find_folder(root, 100000)
    part_one_sol = 0
    for folder in light_folders:
        part_one_sol += folder[1]
    print("SOL PART 1:", part_one_sol)

    total_size = 70000000
    free_space = total_size - root.size()
    free_space = 30000000 - free_space

    folders_part_two = find_folder(root, 0, free_space)
    print(f"SOL PART 2: {min([folder[1] for folder in folders_part_two])=}")


if __name__ == "__main__":
    # main("7-test.txt")
    main("7-input.txt")
