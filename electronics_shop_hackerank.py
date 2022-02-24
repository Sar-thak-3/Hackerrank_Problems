entries = input()
entries = entries.split(" ")
keyboard = input()
keyboard = keyboard.split(" ")
drives = input()
drives = drives.split(' ')
result = -1
for board in keyboard:
    for drive in drives:
        if int(board)+int(drive)>0 and int(board)+int(drive)<=int(entries[0]) and int(board)+int(drive)>result:
            result = int(board)+int(drive)
print(result)            