with open("6-input.txt") as f:
    datastream = f.readline()

def look_for_marker(ds, length):
    for i in range(len(ds)):
        if len(set(ds[0+i:length+i])) == length:
            break
    return i + length

print("PART ONE:", look_for_marker(datastream, 4))
print("PART ONE:", look_for_marker(datastream, 14))