import pandas as pd

# Nickname. If record[1]["NickName"] in nicknames.csv then use the ID. if not create a new table and assign 300, nickname
def check_nickname(record, nicknametable):
    nickname = record[1]["NickName"]
    if type(nickname) != float:
        isnicknamethere = nicknametable.loc[nicknametable['NICKNAME'] == nickname[:25], 'ID']
        if not nicknametable.loc[nicknametable['NICKNAME'] == nickname[:25], 'ID'].empty:
            return isnicknamethere.iloc[0]
        else:
            if type(nickname) != float:
                new_row = {'ID': int(nicknametable.iloc[-1]['ID'] + 1), 'NICKNAME': nickname[:25]}
                nicknametable = nicknametable.append(new_row, ignore_index=True)
                nicknametable.to_csv('nicknames_v01.csv',  index=False)
                return nicknametable.iloc[-1]['ID']
    else:
        return -1
    
def check_playerID(df, name, fname, dob):
    result = df.loc[(df['NAME'] == name) & (df['FNAME'] == fname) & (df['USE'] == True)]
    if not result.empty:
        # if length is 1
        if result.shape[0] == 1:
            return result
        # else
        else:
            resultnew = result.loc[((df['BIRTHDATE']) == float(dob))]
            if not resultnew.empty:
                return resultnew
            else:
                return []
    else:
        return []

yearandteams = {
	1961: 9,
	1962: 9,
	1963: 9,
	1964: 9,
	1965: 9,
	1966: 10,
	1967: 12,
	1968: 14,
	1969: 14,
	1970: 17,
	1971: 17,
	1972: 17,
	1973: 17,
	1974: 18,
	1975: 18,
	1976: 22,
	1977: 22,
	1978: 22,
	1979: 22,
	1980: 23,
	1981: 23,
	1982: 23,
	1983: 23,
	1984: 23,
	1985: 23,
	1986: 23,
	1987: 23,
	1988: 25,
	1989: 27,
	1990: 27,
	1991: 27,
	1992: 27,
	1993: 27,
	1994: 27,
	1995: 29,
	1996: 29,
	1997: 29,
	1998: 29,
	1999: 29,
	2000: 29,
	2001: 29,
	2002: 29,
	2003: 29,
	2004: 30,
	2005: 30,
	2006: 30,
	2007: 30,
	2008: 30,
	2009: 30,
	2010: 30,
	2011: 30,
	2012: 30,
	2013: 30,
	2014: 30,
}

def draftdata(record, teamIDs, draftteam):
    if draftteam == -1:
        return [-1, -1, -1, record[1]['DraftYear'], '--']
    else:
        draftyear = record[1]['DraftYear']
        draftround = record[1]['DraftRound']
        draftpos = record[1]['DraftPos']
        draftteam = teamIDs.loc[teamIDs['2KID'] == draftteam, f'IS{str(draftyear + 1)[2:]}'].values[0]
        pos = draftpos + (draftround - 1) * (yearandteams[draftyear])
        return [pos, draftround, pos, draftyear, draftteam]

def set_position(pos, secondpos):
    poslive = -(pos) + 4
    if secondpos == 5:
        return [poslive, poslive]
    else:
        secondposlive = -(secondpos) + 4
        return [poslive, secondposlive]
    
def set_college(colleges, collegeID, is2005):
    result = colleges.loc[(colleges['2KID'] == collegeID)]
    if result.empty:
        return 319
    elif is2005 and result['IS05'].values[0] == False:
        return 319
    else:
        return result['SCHOOLID'].values[0]
    # check if 2k collegeID is in the csv first. if finds the value then check is2005
    # if is2005 is False then return 319

shoedict = {0: 0, 1: 1, 2: 2, 3: 1, 4: 0, 5: 3, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
def set_shoe_brand(shoe):
    return shoedict[shoe]

rosterdict = {
    "Ros_PG": 4,
    "Ros_SG": 3,
    "Ros_SF": 2,
    "Ros_PF": 1,
    "Ros_C"	: 0,
    "Ros_S6": 5,
    "Ros_S7": 6,
    "Ros_S8": 7,
    "Ros_S9": 8,
    "Ros_S10": 9,
    "Ros_S11": 10,	
    "Ros_S12": 11,
    "Ros_R13": 12,
    "Ros_R14": 13,
    "Ros_R15": 14
}
def set_roster_position(teams_2k, teamid, id):
    row = teams_2k[teams_2k['ID'] == teamid]
    # Find the column of that row that has value 8
    rosterstring = row.filter(like='Ros').eq(id).idxmax(axis=1).values[0]
    return rosterdict[rosterstring]