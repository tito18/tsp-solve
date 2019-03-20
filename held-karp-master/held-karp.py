import itertools
import random
import sys
import time 



def held_karp(dists):
    """
    Implementation of Held-Karp, an algorithm that solves the Traveling
    Salesman Problem using dynamic programming with memoization.

    Parameters:
        dists: distance matrix

    Returns:
        A tuple, (cost, path).
    """
    n = len(dists)

    # Maps each subset of the nodes to the cost to reach that subset, as well
    # as what node it passed before reaching this subset.
    # Node subsets are represented as set bits.
    C = {}

    # Set transition cost from initial state
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)

    # Iterate subsets of increasing length and store intermediate results
    # in classic dynamic programming manner
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

    # We're interested in all bits but the least significant (the start state)
    bits = (2**n - 1) - 1

    # Calculate optimal cost
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)

    # Backtrack to find full path
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    # Add implicit start state
    path.append(0)

    return opt, list(reversed(path))


def generate_distances(n):
    dists = [[0] * n for i in range(n)]

    if n == 4:
        print("hola")
        dists[0][0]=0
        dists[0][1]=2
        dists[0][2]=9
        dists[0][3]=10
        dists[1][0]=1
        dists[1][1]=0
        dists[1][2]=6
        dists[1][3]=4
        dists[2][0]=15
        dists[2][1]=7
        dists[2][2]=0
        dists[2][3]=8
        dists[3][0]=6
        dists[3][1]=3
        dists[3][2]=12
        dists[3][3]=0

    if n == 20:
        dists[0][0]=0
        dists[0][1]=29
        dists[0][2]=28
        dists[0][3]=83
        dists[0][4]=18
        dists[0][5]=26
        dists[0][6]=79
        dists[0][7]=29
        dists[0][8]=59
        dists[0][9]=6
        dists[0][10]=88
        dists[0][11]=62
        dists[0][12]=61
        dists[0][13]=96
        dists[0][14]=36
        dists[0][15]=38
        dists[0][16]=61
        dists[0][17]=48
        dists[0][18]=10
        dists[0][19]=80

        dists[1][0]=29
        dists[1][1]=0
        dists[1][2]=25
        dists[1][3]=64
        dists[1][4]=77
        dists[1][5]=89
        dists[1][6]=80
        dists[1][7]=77
        dists[1][8 ]=20
        dists[1][9]=61
        dists[1][10]=10
        dists[1][11]=8
        dists[1][12]=57
        dists[1][13]=24
        dists[1][14]=39
        dists[1][15]=81
        dists[1][16]=80
        dists[1][17]=49
        dists[1][18]=83
        dists[1][19]=71

        dists[2][0]=28
        dists[2][1]=25
        dists[2][2]=0
        dists[2][3]=42
        dists[2][4]=11
        dists[2][5]=77
        dists[2][6]=74
        dists[2][7]=2
        dists[2][8]=52
        dists[2][9]=19
        dists[2][10]=83
        dists[2][11]=38
        dists[2][12]=26
        dists[2][13]=38
        dists[2][14]=26
        dists[2][15]=49
        dists[2][16]=32
        dists[2][17]=52
        dists[2][18]=44
        dists[2][19]=15

        dists[3][0]=83
        dists[3][1]=64
        dists[3][2]=42
        dists[3][3]=0
        dists[3][4]=81
        dists[3][5]=48
        dists[3][6]=85
        dists[3][7]=85
        dists[3][8]=18
        dists[3][9]=22
        dists[3][10]=86
        dists[3][11]=46
        dists[3][12]=46
        dists[3][13]=19
        dists[3][14]=49
        dists[3][15]=98
        dists[3][16]=30
        dists[3][17]=49
        dists[3][18]=12
        dists[3][19]=52

        dists[4][0]=18
        dists[4][1]=77
        dists[4][2]=11
        dists[4][3]=81
        dists[4][4]=0
        dists[4][5]=65
        dists[4][6]=38
        dists[4][7]=34
        dists[4][8]=5
        dists[4][9]=61
        dists[4][10]=24
        dists[4][11]=9
        dists[4][12]=4
        dists[4][13]=7
        dists[4][14]=97
        dists[4][15]=58
        dists[4][16]=1
        dists[4][17]=37
        dists[4][18]=46
        dists[4][19]=25

        dists[5][0]=26
        dists[5][1]=89
        dists[5][2]=77
        dists[5][3]=48
        dists[5][4]=65
        dists[5][5]=0
        dists[5][6]=95
        dists[5][7]=11
        dists[5][8]=72
        dists[5][9]=29
        dists[5][10]=52
        dists[5][11]=57
        dists[5][12]=60
        dists[5][13]=26
        dists[5][14]=72
        dists[5][15]=99
        dists[5][16]=41
        dists[5][17]=4
        dists[5][18]=26
        dists[5][19]=3

        dists[6][0]=79
        dists[6][1]=80
        dists[6][2]=74
        dists[6][3]=85
        dists[6][4]=38
        dists[6][5]=95
        dists[6][6]=0
        dists[6][7]=95
        dists[6][8]=37
        dists[6][9]=85
        dists[6][10]=34
        dists[6][11]=65
        dists[6][12]=65
        dists[6][13]=98
        dists[6][14]=13
        dists[6][15]=20
        dists[6][16]=56
        dists[6][17]=8
        dists[6][18]=65
        dists[6][19]=12

        dists[7][0]=29
        dists[7][1]=77
        dists[7][2]=2
        dists[7][3]=85
        dists[7][4]=34
        dists[7][5]=11
        dists[7][6]=95
        dists[7][7]=0
        dists[7][8]=7
        dists[7][9]=33
        dists[7][10]=34
        dists[7][11]=67
        dists[7][12]=87
        dists[7][13]=47
        dists[7][14]=20
        dists[7][15]=44
        dists[7][16]=92
        dists[7][17]=65
        dists[7][18]=98
        dists[7][19]=18

        dists[8][0]=59
        dists[8][1]=20
        dists[8][2]=52
        dists[8][3]=18
        dists[8][4]=5
        dists[8][5]=72
        dists[8][6]=37
        dists[8][7]=7
        dists[8][8]=0
        dists[8][9]=49
        dists[8][10]=45
        dists[8][11]=29
        dists[8][12]=18
        dists[8][13]=92
        dists[8][14]=47
        dists[8][15]=56
        dists[8][16]=36
        dists[8][17]=97
        dists[8][18]=66
        dists[8][19]=15

        dists[9][0]=6
        dists[9][1]=61
        dists[9][2]=19
        dists[9][3]=22
        dists[9][4]=61
        dists[9][5]=29
        dists[9][6]=85
        dists[9][7]=33
        dists[9][8]=49
        dists[9][9]=0
        dists[9][10]=50
        dists[9][11]=65
        dists[9][12]=66
        dists[9][13]=61
        dists[9][14]=45
        dists[9][15]=10
        dists[9][16]=86
        dists[9][17]=21
        dists[9][18]=86
        dists[9][19]=37

        dists[10][0]=88
        dists[10][1]=10
        dists[10][2]=83
        dists[10][3]=86
        dists[10][4]=24
        dists[10][5]=52
        dists[10][6]=34
        dists[10][7]=34
        dists[10][8]=45
        dists[10][9]=50
        dists[10][10]=0
        dists[10][11]=46
        dists[10][12]=53
        dists[10][13]=12
        dists[10][14]=59
        dists[10][15]=12
        dists[10][16]=89
        dists[10][17]=3
        dists[10][18]=68
        dists[10][19]=6

        dists[11][0]=62
        dists[11][1]=8
        dists[11][2]=38
        dists[11][3]=46
        dists[11][4]=9
        dists[11][5]=57
        dists[11][6]=65
        dists[11][7]=67
        dists[11][8]=29
        dists[11][9]=65
        dists[11][10]=46
        dists[11][11]=0
        dists[11][12]=91
        dists[11][13]=72
        dists[11][14]=61
        dists[11][15]=56
        dists[11][16]=31
        dists[11][17]=1
        dists[11][18]=13
        dists[11][19]=19

        dists[12][0]=61
        dists[12][1]=57
        dists[12][2]=26
        dists[12][3]=46
        dists[12][4]=4
        dists[12][5]=60
        dists[12][6]=65
        dists[12][7]=87
        dists[12][8]=18
        dists[12][9]=66
        dists[12][10]=53
        dists[12][11]=91
        dists[12][12]=0
        dists[12][13]=52
        dists[12][14]=17
        dists[12][15]=74
        dists[12][16]=93
        dists[12][17]=32
        dists[12][18]=13
        dists[12][19]=41

        dists[13][0]=96
        dists[13][1]=24
        dists[13][2]=38
        dists[13][3]=19
        dists[13][4]=7
        dists[13][5]=26
        dists[13][6]=98
        dists[13][7]=47
        dists[13][8]=92
        dists[13][9]=61
        dists[13][10]=12
        dists[13][11]=72
        dists[13][12]=52
        dists[13][13]=0
        dists[13][14]=60
        dists[13][15]=42
        dists[13][16]=95
        dists[13][17]=14
        dists[13][18]=52
        dists[13][19]=77

        dists[14][0]=39
        dists[14][1]=39
        dists[14][2]=26
        dists[14][3]=49
        dists[14][4]=97
        dists[14][5]=72
        dists[14][6]=13
        dists[14][7]=20
        dists[14][8]=47
        dists[14][9]=45
        dists[14][10]=59
        dists[14][11]=61
        dists[14][12]=17
        dists[14][13]=60
        dists[14][14]=0
        dists[14][15]=66
        dists[14][16]=18
        dists[14][17]=4
        dists[14][18]=18
        dists[14][19]=93

        dists[15][0]=38
        dists[15][1]=81
        dists[15][2]=49
        dists[15][3]=98
        dists[15][4]=58
        dists[15][5]=99
        dists[15][6]=20
        dists[15][7]=44
        dists[15][8]=56
        dists[15][9]=10
        dists[15][10]=12
        dists[15][11]=56
        dists[15][12]=74
        dists[15][13]=42
        dists[15][14]=66
        dists[15][15]=0
        dists[15][16]=47
        dists[15][17]=51
        dists[15][18]=66
        dists[15][19]=19

        dists[16][0]=61
        dists[16][1]=80
        dists[16][2]=32
        dists[16][3]=30
        dists[16][4]=1
        dists[16][5]=41
        dists[16][6]=56
        dists[16][7]=92
        dists[16][8]=36
        dists[16][9]=86
        dists[16][10]=89
        dists[16][11]=31
        dists[16][12]=93
        dists[16][13]=95
        dists[16][14]=18
        dists[16][15]=47
        dists[16][16]=0
        dists[16][17]=44
        dists[16][18]=80
        dists[16][19]=56

        dists[17][0]=48
        dists[17][1]=49
        dists[17][2]=52
        dists[17][3]=49
        dists[17][4]=37
        dists[17][5]=4
        dists[17][6]=8
        dists[17][7]=65
        dists[17][8]=97
        dists[17][9]=21
        dists[17][10]=3
        dists[17][11]=1
        dists[17][12]=32
        dists[17][13]=14
        dists[17][14]=4
        dists[17][15]=51
        dists[17][16]=44
        dists[17][17]=0
        dists[17][18]=99
        dists[17][19]=16

        dists[18][0]=10
        dists[18][1]=83
        dists[18][2]=44
        dists[18][3]=12
        dists[18][4]=46
        dists[18][5]=26
        dists[18][6]=65
        dists[18][7]=98
        dists[18][8]=66
        dists[18][9]=86
        dists[18][10]=68
        dists[18][11]=13
        dists[18][12]=13
        dists[18][13]=52
        dists[18][14]=18
        dists[18][15]=66
        dists[18][16]=80
        dists[18][17]=99
        dists[18][18]=0
        dists[18][19]=55

        dists[19][0]=80
        dists[19][1]=71
        dists[19][2]=15
        dists[19][3]=52
        dists[19][4]=25
        dists[19][5]=3
        dists[19][6]=12
        dists[19][7]=18
        dists[19][8]=15
        dists[19][9]=37
        dists[19][10]=6
        dists[19][11]=19
        dists[19][12]=41
        dists[19][13]=77
        dists[19][14]=93
        dists[19][15]=19
        dists[19][16]=56
        dists[19][17]=16
        dists[19][18]=55
        dists[19][19]= 0

    if n == 21:
        dists[0][0]=0   
        dists[0][1]=29
        dists[0][2]=28
        dists[0][3]=83
        dists[0][4]=18
        dists[0][5]=26
        dists[0][6]=79
        dists[0][7]=29
        dists[0][8]=59
        dists[0][9]=6
        dists[0][10]=88
        dists[0][11]=62
        dists[0][12]=61
        dists[0][13]=96
        dists[0][14]=36
        dists[0][15]=38
        dists[0][16]=61
        dists[0][17]=48
        dists[0][18]=10
        dists[0][19]=80
        dists[0][20]=12

        dists[1][0]=29
        dists[1][1]=0
        dists[1][2]=25
        dists[1][3]=64
        dists[1][4]=77
        dists[1][5]=89
        dists[1][6]=80
        dists[1][7]=77
        dists[1][8 ]=20
        dists[1][9]=61
        dists[1][10]=10
        dists[1][11]=8
        dists[1][12]=57
        dists[1][13]=24
        dists[1][14]=39
        dists[1][15]=81
        dists[1][16]=80
        dists[1][17]=49
        dists[1][18]=83
        dists[1][19]=71
        dists[1][20]=4

        dists[2][0]=28
        dists[2][1]=25
        dists[2][2]=0
        dists[2][3]=42
        dists[2][4]=11
        dists[2][5]=77
        dists[2][6]=74
        dists[2][7]=2
        dists[2][8]=52
        dists[2][9]=19
        dists[2][10]=83
        dists[2][11]=38
        dists[2][12]=26
        dists[2][13]=38
        dists[2][14]=26
        dists[2][15]=49
        dists[2][16]=32
        dists[2][17]=52
        dists[2][18]=44
        dists[2][19]=15
        dists[2][20]=33

        dists[3][0]=83
        dists[3][1]=64
        dists[3][2]=42
        dists[3][3]=0
        dists[3][4]=81
        dists[3][5]=48
        dists[3][6]=85
        dists[3][7]=85
        dists[3][8]=18
        dists[3][9]=22
        dists[3][10]=86
        dists[3][11]=46
        dists[3][12]=46
        dists[3][13]=19
        dists[3][14]=49
        dists[3][15]=98
        dists[3][16]=30
        dists[3][17]=49
        dists[3][18]=12
        dists[3][19]=52
        dists[3][20]=46

        dists[4][0]=18
        dists[4][1]=77
        dists[4][2]=11
        dists[4][3]=81
        dists[4][4]=0
        dists[4][5]=65
        dists[4][6]=38
        dists[4][7]=34
        dists[4][8]=5
        dists[4][9]=61
        dists[4][10]=24
        dists[4][11]=9
        dists[4][12]=4
        dists[4][13]=7
        dists[4][14]=97
        dists[4][15]=58
        dists[4][16]=1
        dists[4][17]=37
        dists[4][18]=46
        dists[4][19]=25
        dists[4][20]=39

        dists[5][0]=26
        dists[5][1]=89
        dists[5][2]=77
        dists[5][3]=48
        dists[5][4]=65
        dists[5][5]=0
        dists[5][6]=95
        dists[5][7]=11
        dists[5][8]=72
        dists[5][9]=29
        dists[5][10]=52
        dists[5][11]=57
        dists[5][12]=60
        dists[5][13]=26
        dists[5][14]=72
        dists[5][15]=99
        dists[5][16]=41
        dists[5][17]=4
        dists[5][18]=26
        dists[5][19]=3
        dists[5][20]=22

        dists[6][0]=79
        dists[6][1]=80
        dists[6][2]=74
        dists[6][3]=85
        dists[6][4]=38
        dists[6][5]=95
        dists[6][6]=0
        dists[6][7]=95
        dists[6][8]=37
        dists[6][9]=85
        dists[6][10]=34
        dists[6][11]=65
        dists[6][12]=65
        dists[6][13]=98
        dists[6][14]=13
        dists[6][15]=20
        dists[6][16]=56
        dists[6][17]=8
        dists[6][18]=65
        dists[6][19]=12
        dists[6][20]=65

        dists[7][0]=29
        dists[7][1]=77
        dists[7][2]=2
        dists[7][3]=85
        dists[7][4]=34
        dists[7][5]=11
        dists[7][6]=95
        dists[7][7]=0
        dists[7][8]=7
        dists[7][9]=33
        dists[7][10]=34
        dists[7][11]=67
        dists[7][12]=87
        dists[7][13]=47
        dists[7][14]=20
        dists[7][15]=44
        dists[7][16]=92
        dists[7][17]=65
        dists[7][18]=98
        dists[7][19]=18
        dists[7][20]=89

        dists[8][0]=59
        dists[8][1]=20
        dists[8][2]=52
        dists[8][3]=18
        dists[8][4]=5
        dists[8][5]=72
        dists[8][6]=37
        dists[8][7]=7
        dists[8][8]=0
        dists[8][9]=49
        dists[8][10]=45
        dists[8][11]=29
        dists[8][12]=18
        dists[8][13]=92
        dists[8][14]=47
        dists[8][15]=56
        dists[8][16]=36
        dists[8][17]=97
        dists[8][18]=66
        dists[8][19]=15
        dists[8][20]=40

        dists[9][0]=6
        dists[9][1]=61
        dists[9][2]=19
        dists[9][3]=22
        dists[9][4]=61
        dists[9][5]=29
        dists[9][6]=85
        dists[9][7]=33
        dists[9][8]=49
        dists[9][9]=0
        dists[9][10]=50
        dists[9][11]=65
        dists[9][12]=66
        dists[9][13]=61
        dists[9][14]=45
        dists[9][15]=10
        dists[9][16]=86
        dists[9][17]=21
        dists[9][18]=86
        dists[9][19]=37
        dists[9][20]=27

        dists[10][0]=88
        dists[10][1]=10
        dists[10][2]=83
        dists[10][3]=86
        dists[10][4]=24
        dists[10][5]=52
        dists[10][6]=34
        dists[10][7]=34
        dists[10][8]=45
        dists[10][9]=50
        dists[10][10]=0
        dists[10][11]=46
        dists[10][12]=53
        dists[10][13]=12
        dists[10][14]=59
        dists[10][15]=12
        dists[10][16]=89
        dists[10][17]=3
        dists[10][18]=68
        dists[10][19]=6
        dists[10][20]=91

        dists[11][0]=62
        dists[11][1]=8
        dists[11][2]=38
        dists[11][3]=46
        dists[11][4]=9
        dists[11][5]=57
        dists[11][6]=65
        dists[11][7]=67
        dists[11][8]=29
        dists[11][9]=65
        dists[11][10]=46
        dists[11][11]=0
        dists[11][12]=91
        dists[11][13]=72
        dists[11][14]=61
        dists[11][15]=56
        dists[11][16]=31
        dists[11][17]=1
        dists[11][18]=13
        dists[11][19]=19
        dists[11][20]=98

        dists[12][0]=61
        dists[12][1]=57
        dists[12][2]=26
        dists[12][3]=46
        dists[12][4]=4
        dists[12][5]=60
        dists[12][6]=65
        dists[12][7]=87
        dists[12][8]=18
        dists[12][9]=66
        dists[12][10]=53
        dists[12][11]=91
        dists[12][12]=0
        dists[12][13]=52
        dists[12][14]=17
        dists[12][15]=74
        dists[12][16]=93
        dists[12][17]=32
        dists[12][18]=13
        dists[12][19]=41
        dists[12][20]=81

        dists[13][0]=96
        dists[13][1]=24
        dists[13][2]=38
        dists[13][3]=19
        dists[13][4]=7
        dists[13][5]=26
        dists[13][6]=98
        dists[13][7]=47
        dists[13][8]=92
        dists[13][9]=61
        dists[13][10]=12
        dists[13][11]=72
        dists[13][12]=52
        dists[13][13]=0
        dists[13][14]=60
        dists[13][15]=42
        dists[13][16]=95
        dists[13][17]=14
        dists[13][18]=52
        dists[13][19]=77
        dists[13][20]=59

        dists[14][0]=39
        dists[14][1]=39
        dists[14][2]=26
        dists[14][3]=49
        dists[14][4]=97
        dists[14][5]=72
        dists[14][6]=13
        dists[14][7]=20
        dists[14][8]=47
        dists[14][9]=45
        dists[14][10]=59
        dists[14][11]=61
        dists[14][12]=17
        dists[14][13]=60
        dists[14][14]=0
        dists[14][15]=66
        dists[14][16]=18
        dists[14][17]=4
        dists[14][18]=18
        dists[14][19]=93
        dists[14][20]=56

        dists[15][0]=38
        dists[15][1]=81
        dists[15][2]=49
        dists[15][3]=98
        dists[15][4]=58
        dists[15][5]=99
        dists[15][6]=20
        dists[15][7]=44
        dists[15][8]=56
        dists[15][9]=10
        dists[15][10]=12
        dists[15][11]=56
        dists[15][12]=74
        dists[15][13]=42
        dists[15][14]=66
        dists[15][15]=0
        dists[15][16]=47
        dists[15][17]=51
        dists[15][18]=66
        dists[15][19]=19
        dists[15][20]=85

        dists[16][0]=61
        dists[16][1]=80
        dists[16][2]=32
        dists[16][3]=30
        dists[16][4]=1
        dists[16][5]=41
        dists[16][6]=56
        dists[16][7]=92
        dists[16][8]=36
        dists[16][9]=86
        dists[16][10]=89
        dists[16][11]=31
        dists[16][12]=93
        dists[16][13]=95
        dists[16][14]=18
        dists[16][15]=47
        dists[16][16]=0
        dists[16][17]=44
        dists[16][18]=80
        dists[16][19]=56
        dists[16][20]=64

        dists[17][0]=48
        dists[17][1]=49
        dists[17][2]=52
        dists[17][3]=49
        dists[17][4]=37
        dists[17][5]=4
        dists[17][6]=8
        dists[17][7]=65
        dists[17][8]=97
        dists[17][9]=21
        dists[17][10]=3
        dists[17][11]=1
        dists[17][12]=32
        dists[17][13]=14
        dists[17][14]=4
        dists[17][15]=51
        dists[17][16]=44
        dists[17][17]=0
        dists[17][18]=99
        dists[17][19]=16
        dists[17][20]=92

        dists[18][0]=10
        dists[18][1]=83
        dists[18][2]=44
        dists[18][3]=12
        dists[18][4]=46
        dists[18][5]=26
        dists[18][6]=65
        dists[18][7]=98
        dists[18][8]=66
        dists[18][9]=86
        dists[18][10]=68
        dists[18][11]=13
        dists[18][12]=13
        dists[18][13]=52
        dists[18][14]=18
        dists[18][15]=66
        dists[18][16]=80
        dists[18][17]=99
        dists[18][18]=0
        dists[18][19]=55
        dists[18][20]=58

        dists[19][0]=80
        dists[19][1]=71
        dists[19][2]=15
        dists[19][3]=52
        dists[19][4]=25
        dists[19][5]=3
        dists[19][6]=12
        dists[19][7]=18
        dists[19][8]=15
        dists[19][9]=37
        dists[19][10]=6
        dists[19][11]=19
        dists[19][12]=41
        dists[19][13]=77
        dists[19][14]=93
        dists[19][15]=19
        dists[19][16]=56
        dists[19][17]=16
        dists[19][18]=55
        dists[19][19]= 0
        dists[19][20]=37
        
        dists[20][0]=56
        dists[20][1]=28
        dists[20][2]=20
        dists[20][3]=81
        dists[20][4]=71
        dists[20][5]=24
        dists[20][6]=92
        dists[20][7]=54
        dists[20][8]=13
        dists[20][9]=85
        dists[20][10]=66
        dists[20][11]=97
        dists[20][12]=43
        dists[20][13]=81
        dists[20][14]=15
        dists[20][15]=64
        dists[20][16]=35
        dists[20][17]=86
        dists[20][18]=37
        dists[20][19]=9
        dists[20][20]=0
            
    """
    else:
        for i in range(n):
            for j in range(i+1, n):
                dists[i][j] = dists[j][i] = random.randint(1, 99)
    """

    return dists


def read_distances(filename):
    dists = []
    #with open(filename, 'rb') as f:
    #    for line in f:
    #        # Skip comments
    #        if line[0] == '#':
    #            continue
    #
    #        dists.append(map(int, map(str.strip, line.split(','))))*/

    return dists


if __name__ == '__main__':
    start = time.time()

    arg = sys.argv[1]

    if arg.endswith('.csv'):
        dists = read_distances(arg)
    else:
        dists = generate_distances(int(arg))

    # Pretty-print the distance matrix
    for row in dists:
        print(''.join([str(n).rjust(3, ' ') for n in row]))

    print('')

    print(held_karp(dists))

    end = time.time()
    print("\n",end - start)


