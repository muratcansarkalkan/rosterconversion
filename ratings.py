def calc_overall_2005(attributes, position):
    table4 = [100,100,100,100,120,100,100,100,120,100,100,120,120,100,120,100,100,0,100,100,0,100]
    table3 = [100,120,100,100,100,100,100,100,120,100,100,120,120,100,120,100,100,0,100,100,0,100]
    table2 = [100,120,100,100,100,100,100,100,120,100,100,120,120,100,120,100,100,0,100,100,0,100]
    table1 = [100,100,100,120,100,120,120,120,100,100,100,100,100,100,100,120,100,0,100,120,0,100]
    table0 = [100,100,100,120,100,120,120,120,100,100,100,100,100,100,100,120,100,0,100,120,0,100]
    if position == 0:
        table = table0
    elif position == 1:
        table = table1
    elif position == 2:
        table = table2
    elif position == 3:
        table = table3
    elif position == 4:
        table = table4
    multiplied = [a * b for a, b in zip(table, attributes)]
    playervalue = round(33 * sum(multiplied) / 1000)
    overall = round((playervalue-1500)*0.00025641025*99)
    if overall > 99:
        overall = 99
    elif overall < 0:
        overall = 0
    attributes_new = [overall, playervalue]
    attributes_new += attributes
    return attributes_new

def calc_overall_06(attributes, position):
    table4 = [100,100,100,100,120,100,100,100,120,100,100,120,120,100,120,100,100,0,100,100,0,0]
    table3 = [100,120,100,100,100,100,100,100,120,100,100,120,120,100,120,100,100,0,100,100,0,0]
    table2 = [100,120,100,100,100,100,100,100,120,100,100,120,120,100,120,100,100,0,100,100,0,0]
    table1 = [100,100,100,120,100,120,120,120,100,100,100,100,100,100,100,120,100,0,100,120,0,0]
    table0 = [100,100,100,120,100,120,120,120,100,100,100,100,100,100,100,120,100,0,100,120,0,0]
    if position == 0:
        table = table0
    elif position == 1:
        table = table1
    elif position == 2:
        table = table2
    elif position == 3:
        table = table3
    elif position == 4:
        table = table4
    multiplied = [a * b for a, b in zip(table, attributes)]
    playervalue = round(sum(multiplied) * 0.01)
    overall = round((playervalue-100)*0.06666667)
    if overall > 99:
        overall = 99
    elif overall < 0:
        overall = 0
    attributes_new = [overall, playervalue]
    attributes_new += attributes
    return attributes_new

def calc_shoot_range(basethree):
    if basethree < 3:
        return 12
    elif basethree < 10:
        return 13
    elif basethree < 20:
        return 15
    elif basethree < 30:
        return 18
    elif basethree < 50:
        return 20
    elif basethree < 65:
        return 23      
    else:
        return 25

def calc_dunkpack_06(height, dunkRating, weight):
    # 73, 180
    if height < 72:
        if dunkRating > 85:
            return 14
        elif dunkRating > 59:
            return 5
        else:
            return 1
    elif height >= 78:
        if height >= 83:
            if height >= 86:
                if dunkRating > 30:
                    return 6
                else:
                    return 2
            elif dunkRating <= 30:
                return 2
            elif dunkRating < 60:
                return 11
            elif dunkRating >= 85:
                if weight < 300:
                    return 15
                else:
                    return 6
            else:
                return 6
        else:
            if dunkRating <= 30:
                return 2
            elif dunkRating < 50:
                return 11
            elif dunkRating < 70:
                return 8
            elif dunkRating >= 85:
                return 15
            else:
                return 6
    else:
        if dunkRating <= 49:
            return 1
        elif dunkRating < 70:
            return 4
        elif dunkRating >= 85:
            return 9
        else:
            return 16

def calc_scorearea(height, dribble, threePtRating, insideScoring):
    result = 1
    
    if height <= 77 and dribble >= 70:
        result = 6
    
    if height >= 78:
        if threePtRating < 70:
            if insideScoring >= 70:
                result = 9
                return result
            else:
                return 4
        else:
            if insideScoring < 70:
                result = 4
            else:
                result = 10
    
    if height <= 77 and dribble < 70:
        return 2
    
    return result

def calc_threeptsty(height, threePtRating):
    if height <= 73:
        if threePtRating >= 40:
            return 1
        else:
            return 3
    
    if height <= 77:
        if threePtRating >= 40:
            return (threePtRating < 70) + 4
        return 6
    
    if height <= 80:
        if threePtRating >= 40:
            return 2 * (threePtRating < 70) + 5
        return 6
    
    if height > 83:
        if threePtRating >= 50:
            return 2 * (threePtRating < 80) + 8
        else:
            return 9
    elif threePtRating >= 40:
        return 2 * (threePtRating >= 70) + 6
    else:
        return 10

def calc_destiny(birthyear, is2005):
    if is2005:
        age20 = 1984
    else:
        age20 = 1985
    gap = age20 - birthyear
    if gap >= 16:
        return 8
    elif gap >= 14:
        return 7
    elif gap >= 12:
        return 6
    elif gap >= 10:
        return 5
    elif gap >= 8:
        return 4
    elif gap >= 5:
        return 3
    elif gap >= 3:
        return 2
    else:
        return 1

def calc_attributes(record, is2005, multiplier, deducter):

    attributes = []
    fgpbase = int(multiplier*(max(record[1]['SShtCls'], record[1]['SShtMed']))-deducter)
    attributes.append(fgpbase)
    threeptbas = int(multiplier*(record[1]['SSht3PT'])-deducter)
    attributes.append(threeptbas)
    ftpbase = record[1]["SShtFT"]
    attributes.append(ftpbase)
    dnkability = int(multiplier*(record[1]['SDunk'])-deducter)
    attributes.append(dnkability)
    stlability = int(multiplier*(record[1]['SSteal'])-deducter)
    attributes.append(stlability)
    blkability = int(multiplier*(record[1]['SBlock'])-deducter)
    attributes.append(blkability)
    oreability = int(multiplier*(record[1]['SOReb'])-deducter)
    attributes.append(oreability)
    dreability = int(multiplier*(record[1]['SDReb'])-deducter)
    attributes.append(dreability)
    balability = int(multiplier*(record[1]['SPass'])-deducter)
    attributes.append(balability)
    offability = int(multiplier*(record[1]['SOAwar'])-deducter)
    attributes.append(offability)
    defability = int(multiplier*(record[1]['SDAwar'])-deducter)
    attributes.append(defability)
    speed = int(multiplier*(record[1]['SSpeed'])-deducter)
    attributes.append(speed)
    quick = int(multiplier*(record[1]['SQuick'])-deducter)
    attributes.append(quick)
    jump = int(multiplier*(record[1]['SVertical'])-deducter)
    attributes.append(jump)
    dribble = int(multiplier*(record[1]['SBallHndl'])-deducter)
    attributes.append(dribble)
    dstrength = int(multiplier*(record[1]['SStrength'])-deducter)
    attributes.append(dstrength)
    dhardy = int(multiplier*(record[1]['SDurab'])-deducter)
    attributes.append(dhardy)
    dshootrang = calc_shoot_range(threeptbas)
    attributes.append(dshootrang)
    fatigue = int(multiplier*(record[1]['SStamina'])-deducter)
    attributes.append(fatigue)
    insidesc = int((multiplier*0.5*(record[1]['SShtLoP'] + record[1]['SShtCls']))-deducter)
    attributes.append(insidesc)
    threeatt2k = record[1]['T3PTShots']
    allatts2k = record[1]['TInsShots'] + record[1]['TCloseSht'] + record[1]['TMidShots'] + threeatt2k
    threeatt = int((100 * threeatt2k) / allatts2k)
    attributes.append(threeatt)
    primacy = record[1]['TTouches']
    attributes.append(primacy)

    position = -(record[1]['Pos']) + 4
    if is2005:
        attributes_new = calc_overall_2005(attributes, position)
    else:
        attributes_new = calc_overall_06(attributes, position)
    height = int(record[1]['Height'] / 2.54)
    attributes_new.append(calc_scorearea(height, dribble, threeptbas, insidesc))
    return attributes_new