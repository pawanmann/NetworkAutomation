# def add(a,b):
#     return a+b
#
# def add(a,b,c=5):
#     return a+b+c
# print(add(1,2))




from pprint import pprint


# DICTIONARY representing a device
device = dict()
device["name"] = "sbx-n9kv-ao"
device["vendor"] = "cisco"
device["model"] = "Nexus9000 C9300v Chassis"
device["os"] = "nxos"
device["version"] = "9.3(3)"
device["ip"] = "10.1.1.1"

# SIMPLE PRINT
print("\n_____ SIMPLE PRINT ____________________")
print("device:", device)
print("device name:", device["name"])

# PRETTY PRINT
print("\n_____ PRETTY PRINT ____________________")
pprint(device)

# FOR LOOP, NICELY FORMATTED PRINT
print("\n_____ FOR LOOP, USING F-STRING ____________________")
for key, value in device.items():
    print(f"{key:>20s} : {value}")