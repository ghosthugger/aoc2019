import math


def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def inLineOfSight(x1,y1,x2,y2,xl,yl):
    if (distance(x1,y1,xl,yl) + distance(x2,y2,xl,yl) - distance(x1,y1,x2,y2) < 0.000001) :
        return 1
    return 0



def visible(asteroids):
    res = []
    for start in asteroids:
        count = 0
        for end in asteroids:
            ilos = 0
            for sight in asteroids:
                if not sight == start and not sight == end:
                    ilos += inLineOfSight(start[0], start[1], end[0], end[1], sight[0], sight[1])

            if (ilos == 0):
                count += 1

        res.append((start, count - 1))
    res.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in res]


def main():

    c = [(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1)]
    for a in c:
        print(a,math.atan2(a[1],a[0]) + math.pi/2)


    map= """
.#..#
.....
#####
....#
...##"""

    map = """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""


    map = """
##.#..#..###.####...######
#..#####...###.###..#.###.
..#.#####....####.#.#...##
.##..#.#....##..##.#.#....
#.####...#.###..#.##.#..#.
..#..#.#######.####...#.##
#...####.#...#.#####..#.#.
.#..#.##.#....########..##
......##.####.#.##....####
.##.#....#####.####.#.####
..#.#.#.#....#....##.#....
....#######..#.##.#.##.###
###.#######.#..#########..
###.#.#..#....#..#.##..##.
#####.#..#.#..###.#.##.###
.#####.#####....#..###...#
##.#.......###.##.#.##....
...#.#.#.###.#.#..##..####
#....#####.##.###...####.#
#.##.#.######.##..#####.##
#.###.##..##.##.#.###..###
#.####..######...#...#####
#..#..########.#.#...#..##
.##..#.####....#..#..#....
.###.##..#####...###.#.#.#
.##..######...###..#####.#"""


    map ="""
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""


    width = 20 #26 # 10 #26 #5
    asteroids = []
    pos = 0
    map = map.replace("\n", "")
    for p in map:
        x = pos % width
        y = int(pos / width)
        if(map[pos] == "#"):
            asteroids.append((x,y))
        pos = pos +1

    print(asteroids)

    res = visible(asteroids)
    best = res[0]
    print(res)

    deb = [(r,math.atan2(r[1] - best[1], r[0] - best[0]) + math.pi/2) for r in res]

    deb2 = []
    total_angle = 0
    last_angle = 0
    for d in deb:
        angle = d[1]
        if angle < 0:
            angle += 2 * math.pi

        delta_angle = angle - last_angle
        total_angle += delta_angle
        deb2.append((d[0], total_angle))
        last_angle = angle

    deb2.sort(key=lambda x: x[1])
    print(deb2)

    vapor_order = []
    while(len(vapor_order) < 200):
        res.sort(key=lambda x: math.atan2(x[1] - best[1], x[0] - best[0]) + math.pi/2, reverse=True)
        #take at most one turn
        for i in range(10):
            asteroids.remove(res[0])
            vapor_order.append(res[0])
            res.remove(res[0])

        res = visible(asteroids)
    print(vapor_order)


#    print(res[199])
if __name__ =="__main__":
    main()
