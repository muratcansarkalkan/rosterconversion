import pandas as pd
import random

skintonedict = {
    0: 4,
    1: 3,
    2: 3,
    3: 2,
    4: 2,
    5: 0
}
def set_skintone(skintone):
    return skintonedict[skintone]

bodytypedict = {
    0: 0,
    1: 1,
    2: 3,
    3: 2,
}
def set_bodytype(bodytype):
    return bodytypedict[bodytype]

def select_random_pkg(df, skintone):
    plyrs_with_val = df[df['SKINTONE'] == skintone]['GENERIC']
    pkg = plyrs_with_val.sample().iloc[0]
    return pkg

# I think eye color is used from CF texture.
eyecolordict = {
    0: 3,
    1: 1,
    2: 3,
    3: 2,
    4: 1,
    5: 4
}
def set_eyecolor(eyecolor):
    return eyecolordict[eyecolor]

sockdict = {
    0: 1,
    1: 1,
    2: 2,
    3: 2,
    4: 3,
    5: 5,
    6: 3,
    7: 3,
    8: 4
}

def set_sock(sock):
    return sockdict[sock]

def set_finger(finger):
    if finger >= 1:
        return 1
    else:
        return finger
    
wristdict = {
    0: 0,
    1: 5,
    2: 1,
    3: 1,
    4: 1,
    5: 3,
    6: 7,
    7: 3,
    8: 3,
    9: 5,
    10: 5
}

def set_wrist(wrist):
    return wristdict[wrist]

    # if RghtArm is not zero, then bicepband is 3
    # if RghtElb is 1, then elbowband is 3
    # if RghtElb is 2-5-6, then elbowband is 1
    # if RghtElb is 3-4-7, then forearmband is 1

def set_arm(arm2k, elbow2k):
    bicep, elbow, forearm = 0, 0, 0
    if arm2k != 0:
        bicep = 3
    if elbow2k != 0:
        if elbow2k == 1:
            elbow = 3
        elif elbow2k == 2 or elbow2k == 5 or elbow2k == 6:
            elbow = 1
        else:
            forearm = 1
    return bicep, elbow, forearm

kneedict = {
    0: 0,
    1: 1,
    2: 1,
    3: 1,
    4: 3,
    5: 5,
}

lowlegdict = {
    0: 0,
    1: 3,
    2: 5,
    3: 1,
    4: 1,
    5: 8,
    6: 8,
    7: 5
}

def set_legs(knee_2k, lowleg_2k):
    knee = kneedict[knee_2k]
    lowleg = lowlegdict[lowleg_2k]
    return knee, lowleg