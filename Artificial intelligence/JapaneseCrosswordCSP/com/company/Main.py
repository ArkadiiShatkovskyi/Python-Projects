import com.company.ForwardChecking
import com.company.BackTracking
import com.company.Data
import copy


def main():
    n = 100
    r = 6
    bt = com.company.BackTracking.BackTracking(6)
    #bt = com.company.BackTracking.BackTracking(6, sortMethod=sortElements)
    bt.run()
    #fw = com.company.ForwardChecking.ForwardChecking(6)
    #fw = com.company.ForwardChecking.ForwardChecking(6, sortMethod=sortElements)
    #fw.run()
    '''
    testFC(n, r)
    testBT(n, r)
    '''

def sortElements(srows, scolumns):
    tempList = []
    tempColumns = []
    tempRows = []
    rows = copy.deepcopy(srows)
    columns = copy.deepcopy(scolumns)
    for i in range(0, len(scolumns)):
        tempColumns.append(len(scolumns[i].getVariants()))
        tempRows.append(len(srows[i].getVariants()))
    for i in range(0, len(scolumns)*2):
        minR = min(tempRows) if len(tempRows) > 0 else False
        minC = min(tempColumns) if len(tempColumns) > 0 else False
        if minR != False and minC == False or minR != False and minR <= minC:
            indexR = tempRows.index(minR)
            tempList.append(copy.deepcopy(rows[indexR]))
            tempRows.remove(tempRows[indexR])
            rows.remove(rows[indexR])
        elif minC != False:
            indexC = tempColumns.index(copy.deepcopy(min(tempColumns)))
            tempList.append(columns[indexC])
            tempColumns.remove(tempColumns[indexC])
            columns.remove(columns[indexC])
    return tempList

def testFC(n, reques):
    tm = 0
    sets = 0
    for i in range(0, n):
        fw = com.company.ForwardChecking.ForwardChecking(reques)
        temp = fw.run()
        tm += temp[0]
        sets += temp[1]
    print("Final result of FC tm: " + str(tm / n) + ", sets: " + str(sets / n))

def testBT(n, reques):
    tm = 0
    sets = 0
    for i in range(0, n):
        bt = com.company.BackTracking.BackTracking(reques)
        temp = bt.run()
        tm += temp[0]
        sets += temp[1]
    print("Final result of BT tm: " + str(tm / n) + ", sets: " + str(sets / n))

if __name__ == "__main__":
    main()