import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = False

restart_pos = {
    'x': 927,
    'y': 591
}

door_pos = {
    'x':[485, 670, 855, 1040, 1225, 1410],
    'y':[435,685]
}

speed_ms = 1

def auto_detect():
    door_status = []

    can_open = []

    door_item = []

    pair_door = []

    already_pair = []

    pyautogui.click(950,600)
    pyautogui.sleep(1.7)

    for i in range(len(door_pos['y'])):
        door_status.append([])
        for j in range(len(door_pos['x'])):
            door_status[i].append({
                "R":pyautogui.pixel(door_pos['x'][j], door_pos['y'][i]).__getitem__(0),
                "G":pyautogui.pixel(door_pos['x'][j], door_pos['y'][i]).__getitem__(1),
                "B":pyautogui.pixel(door_pos['x'][j], door_pos['y'][i]).__getitem__(2)
            })

    #print(door_status)

    for i in range(len(door_pos['y'])):
        can_open.append([])
        for j in range(len(door_pos['x'])):
            if(door_status[i][j]['R'] > 5):
                can_open[i].append(False)
            else:
                can_open[i].append(True)
    
    #print(can_open)

    for i in range(len(door_pos['y'])):
        door_item.append([])
        for j in range(len(door_pos['x'])):
            if(can_open[i][j]):
                pyautogui.click(door_pos['x'][j], door_pos['y'][i])
                pyautogui.sleep(0.1)
                door_item[i].append({
                    "R":pyautogui.pixel(door_pos['x'][j], door_pos['y'][i]).__getitem__(0),
                    "G":pyautogui.pixel(door_pos['x'][j], door_pos['y'][i]).__getitem__(1),
                    "B":pyautogui.pixel(door_pos['x'][j], door_pos['y'][i]).__getitem__(2)
                })
            else:
                door_item[i].append(None)

    #print(door_item)

    for i in range(len(door_pos['y'])):
        for j in range(len(door_pos['x'])):
            now_select = door_item[i][j]
            if(now_select == None):
                continue
            else:
                for k in range(len(door_pos['y'])):
                    for l in range(len(door_pos['x'])):
                        if(k == i and l == j):
                            continue
                        if([door_pos['x'][l], door_pos['y'][k]] in already_pair):
                            continue
                        if(is_same_block_color(now_select, door_item[k][l])):
                            pair_door.append([
                                {"x":door_pos['x'][j], "y":door_pos['y'][i]},
                                {"x":door_pos['x'][l], "y":door_pos['y'][k]}
                            ])
                            already_pair.append([door_pos['x'][j], door_pos['y'][i]])


    print(pair_door)


    for i in range(len(pair_door)):
        for j in range(len(pair_door[i])):
            pyautogui.click(pair_door[i][j]['x'], pair_door[i][j]['y'])

def restart():
    pyautogui.click(restart_pos['x'], restart_pos['y'])

def is_same_block_color(RGB_A, RGB_B):
    if(RGB_A == None or RGB_B == None):
        return False
    
    range_tolerate = 15

    RGB_R_range = {
        "max" : RGB_A["R"] + range_tolerate,
        "min" : RGB_A["R"] - range_tolerate
    }

    RGB_G_range = {
        "max" : RGB_A["G"] + range_tolerate,
        "min" : RGB_A["G"] - range_tolerate
    }

    RGB_B_range = {
        "max" : RGB_A["B"] + range_tolerate,
        "min" : RGB_A["B"] - range_tolerate
    }

    if(RGB_R_range['max'] >= RGB_B["R"] >= RGB_R_range['min'] and RGB_G_range['max'] >= RGB_B["G"] >= RGB_G_range['min'] and RGB_B_range['max'] >= RGB_B["B"] >= RGB_B_range['min']):
        return True
    else:
        return False
   
             
def main():
    for i in range(3):
        pyautogui.sleep(1)
        print(3 - i)

    for i in range(10):
        auto_detect()

    restart()

for i in range(1):
    main()