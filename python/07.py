from dataclasses import dataclass, field
import sys
input = open(sys.argv[1], 'r').read().split("\n")


@dataclass
class Node:
    name: str
    up: None = None
    size_of_files: int = 0
    children: list['Node'] = field(default_factory=list)

    def child(self, name):
        for child in self.children:
            if child.name == name:
                return name

        new_child = Node(name, self)
        self.children.append(new_child)
        return new_child

    def dfs(self):
        yield self
        for child in self.children:
            yield from child.dfs()

    def size(self):
        size_of_children = sum(child.size() for child in self.children)
        return size_of_children + self.size_of_files


input = input[1:]
root = Node("/")
cursor = root


def parse(lines):
    for line in lines:
        global root
        global cursor
        if line == "$ cd ..":
            cursor = cursor.up
        elif line.startswith("$ cd"):
            name = line.split(' ')[2]
            child = cursor.child(name)
            cursor = child
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            pass
        else:  # is a file
            [size, name] = line.split(' ')
            cursor.size_of_files += int(size)


parse(input)

part1 = 0
for node in root.dfs():
    size = node.size()
    if size <= 100000:
        part1 += size

print(part1)

free = 70000000 - root.size()
needed = 30000000
smallest = 70000000
name = None

for node in root.dfs():
    size = node.size()
    if size < smallest and free + size >= needed:
        smallest = size
        name = node.name

print(name, smallest)
