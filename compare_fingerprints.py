import numpy as np

def correlation(listx, listy, offset, min_overlap=20):
    
    #Apply the offset. 
    if offset > 0: 
        #If the offset is positive, shift listx to the right
        listx = listx[offset:]
        listy = listy[:len(listx)]
    elif offset < 0:
        #If the offset is negative, shift listy to the right
        offset = -offset
        listy = listy[offset:]
        listx = listx[:len(listy)]
    
    #If either list is less than min_overlap return  None
    if min(len(listx), len(listy)) < min_overlap:
        return None
    
    #Trim listx and listy to be the shorter of the two lists
    if len(listx) > len(listy):
        listx = listx[:len(listy)]
    elif len(listx) < len(listy):
        listy = listy[:len(listx)]
    
    #Start a counter variable
    distance = 0
    for i in range(len(listx)):
        #Represent the two numbers as binary strings and produce a new binary number that is 1 wherever the two are different and 0 where they are the same
        #For example, 000110010 and 000010011 produce 00010001 (i.e., the two inputs differ in two places)
        bits=bin(((1 << 32) - 1) & (listx[i] ^ listy[i])) #Ref: https://stackoverflow.com/a/28383647
        #Add the number of ones (number of differences between the inputs) to the counter dividing by 32
        #This is Hamming distance - https://en.wikipedia.org/wiki/Hamming_distance, but normalized to fall between zero and one since the numbers coming in are 32-bit integers
        distance += (bits.count("1")/32)
    
    distance=distance/len(listx) #Normalize to fall between 0 and 1 by dividing by the number of comparisons
    #Return the similarity, which is 1 minus distance
    return 1-distance
  
def get_score(first, second, span=300, step=1):
    if span > min(len(first), len(second)):
        span = min(len(first), len(second)) -1
    
    corr = []
    for offset in range(-span, span + 1, step):
        corr.append(correlation(first, second, offset))
    
    max_corr=0
    max_corr_offset=0
    for i,c in enumerate(corr):
        if c!=None and c>max_corr:
            max_corr=c
            max_corr_offset=i-span
    return max_corr

if __name__=="__main__":
    #Two audio "fingerprints".

    fingera = [-484795100, -485819100, -485855964, -485870236, -485816347, 1648953255, 1657341862, -494331978, -494397546, -494389370, -494389370, -494389882, -494324346, -477481593, -241554043, -256217660, -257234620, -253105900, -253122284, -253121788, -445929716, -411061476, -142757092, -142741188, -146968264, -149082056, -149155541, -182713046, 1935609706, 1926106090, 1993280474, 1989950922, 1990141386, 1453203658, 1474220234, 1423491147, 1415098379, 337359899, 1413127451, 1413127039, 1424662127, 1420596847, 1975288447, 1996276559, 1987965725, 1983832940, 1983275756, 1983260392, -147444072, 1970674328, 1425345193, 1421086635, 1962171835, 1962206362, 1962205274, 1974988863, 1471057949, 1386917900, 1391124492, 1378541580, 1378562076, 1395268668, 1396341740, 1467677421, 1404820143, 1923665646, 1923662430, 1923646027, 1382650313, 1378525325, 1378541725, 1379557565, 1394159789, 1394147501, 1360728495, 1356740270, 1354709758, 1353521742, 1353464590, 279718158, 15232270, 1084880134, 1168871686, 1202422022, 116097046, 103456850, 103538898, 36364419, 36327827, 36308663, 65670823, 29313701, 297626293, 301756117, 7137109, 2941269, 2941237, 2941221, 275763493, 285099317, 285100293, 285100293, 285133077, 334293285, 317516583, 317515542, 309166854, 309297430, 304972086, 287097190, 269283814, 269287394, 269212386, 1355407075, 1351210977, 1904866256, 1921769920, 1390141888, 1383768900, 1383765764, 1395560212, 1932429620, 1898821669, 1898752039, 1898753071, 1902945325, 1937540156, 1937687676, 1933493460, 1933463684, 1932996740, 1903440288, 1906582180, -239848795, -239725929, -174705010, -170120554, -715380058, -736347226, -602138210, -597738034, 1574790414, 1576874766, 1542390542, 1517163022, 1517167118, 1517167399, 1525228837, 1542982957, 1498955263, 1497902271, 424160671, 432730511, 432718221, 499827085, 533250492, 524854252, 492348200, 360363560, 360361512, 292465177, 1366211337, 1345296649, 1345096793, 1345096888, 1883030680, 1904132232, 1945817480, 1924854712, 1924850601, 1924916155, 1920528890, 1933362666, 1883027754, 1883155242, 1887353098, 1890499594, 1890099210, 1923653646, 1928175631, 1916702733, 1646182508, 1662969324, 1628334828, 1628310189, 559287181, 869600655, 854855822, 846528718, 846659787, 846660409, 871703080, 817180200, 817195565, 817359375, 280472079, 280276751, 1354006538, 1945927754, 1920958682, 1916698875, 1916711017, 1646178153, 1649207913, 1632430697, 1615656648, 1879888585, 1879888585, 1880048377, 1883652712, -254847124, -258081283, -241174035, -241243657, -207705722, -203510394, -229211002, -233406330, -233324314, -231223070, -232296350]

    fingerb = [-447438322, -1525632482, -1523535313, -1523523025, -1523555795, -1524620699, -1524628507, -1520171593, -1478226793, -1482422123, -1481881452, -1481811756, -1481709500, -1480659956, -1480679412, -402743028, -411045604, -146804456, -149082056, -182710229, -182713046, -211873942, 1942883306, 1926171642, 1989943242, 1990010314, 1453203658, 1474191562, 1423687755, 1415090187, 1410970651, 1413135643, 1413127039, 1416272495, 1420400239, 1975288423, 2013037391, 1987892045, 1983832957, 1983800172, 1983259368, -147444072, 1970674328, 1962347193, 1421086635, 1957973418, 1962210458, 1962206298, 1974857754, 2007928863, 1454026765, 1391124492, 1382735884, 1378578460, 1395268668, 1463433580, 1467640557, 1471871727, 1941490414, 1923663582, 1923646031, 1390969291, 1378529421, 1378541709, 1379557565, 1379479725, 1394081965, 1394540975, 1365128874, 1354710778, 1353521742, 1353464334, 11283214, 15231246, 15328526, 1152094470, 1202422022, 132874262, 107646994, 103473362, 36364434, 36335747, 36325299, 65670823, 62605991, 297630375, 297561815, 275572567, 2941269, 2941205, 2941221, 275763493, 285098341, 285101317, 285100293, 285133061, 300808485, 317516581, 317515543, 309170966, 309297430, 309166390, 289194342, 269275622, 269281250, 269209314, 1347149539, 1351210721, 1367995376, 1921770432, 1390141888, 1383768900, 1383774020, 1382715140, 1936623892, 1936701493, 1898752039, 1898753071, 1902947373, 1937544252, 1937753148, 1933493460, 1933459652, 1933455492, 1903440288, 1910776740, -240897371, -239660361, -239725938, -174248314, -715380058, -719553626, -602138186, -597721650, -572562098, 1576870670, 1609368334, 1517158926, 1517167118, 1516905279, 1525359917, 1541936429, 1501040127, 1498950847, 1497902239, 424306063, 432722319, 432718221, 499696028, 524870636, 492348200, 492480040, 360365608, 359574041, 1366211081, 1362073865, 1345095769, 1345096952, 1899807928, 1904132248, 1937686920, 1928000440, 1924850345, 1924916139, 1928913338, 1931265514, 1880938858, 1883224362, 1887353114, 1894694154, 1890099210, 1940430862, 1927847951, 1919848461, 1916715132, 1662969324, 1896770284, 1628330668, 542509965, 836177295, 854855822, 846528654, 846659787, 846659961, 871707176, 816918056, 817195565, 817359375, 280472079, 280276495, 1354006798, 1912373322, 1920827466, 1916436731, 1916702825, 1914613096, 1649257064, 1665985128, 1615658696, 1879888584, 1879888585, 1880081113, 1879458408, -263235736, -253895315, -257959427, -241243657, -207689322, -203510394, -229211002, -233406330, -233324298, -231223070, -231247774, -210804638, -478387358, -511942046, -505916874, -506772977, -477475315, -1484076532]

    #Each fingerprint is a list of 32-bit integers

    s=get_score(fingera,fingerb)
    if abs(s-0.921875)<0.0001:
        print(f"The code produced the correct output:  {s}")
    else:
        print(f"The code did not produce the correct output: {s}")
