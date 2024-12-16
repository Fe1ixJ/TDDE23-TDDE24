lastnames = []

lastnames.append(("Hans", "Müller"))
lastnames.append(("Peter", "Schmidt"))

for entry in lastnames:
    if entry[0] == "Hans":
        print(entry[1])

def createmap():
    return []

def setmap(map_obj, key, value):
    map_obj.append((key, value))

def getmap(map_obj, key):
    return [entry[1] for entry in map_obj if entry[0] == key][0]

lastnames = createmap()

setmap(lastnames, key="Hans2", value="Müller2")
setmap(lastnames, key="Peter2", value="Schmidt2")

print(getmap(lastnames, "Hans2"))

lastnames[0] = 42
print(lastnames)

print(getmap(lastnames, "Jonas"))