import sys
input = open(sys.argv[1], 'r').read()

def start_of(data, n):
    # this won't work right at the start (and maybe end) but I'm guessing the
    # puzzle won't do that.
    for i in range(len(data) - n):
        window = data[i:i+n]
        if len(set(window)) == n:
            return i + n

print(start_of(input, 4))
print(start_of(input, 14))
