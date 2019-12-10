import math


def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def inLineOfSight(x1,y1,x2,y2,xl,yl):
    if (distance(x1,y1,xl,yl) + distance(x2,y2,xl,yl) - distance(x1,y1,x2,y2) < 0.000001) :
        return 1
    return 0




def main():

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



    width = 26 # 10 #26 #5
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

    res = []
    for start in asteroids:
        count = 0
        for end in asteroids:
            ilos = 0
            for sight in asteroids:
                if not sight == start and not sight == end:
                    ilos += inLineOfSight(start[0], start[1], end[0], end[1], sight[0], sight[1])

            if(ilos == 0):
                count += 1

        res.append((start, count-1))

    res.sort(key=lambda x:x[1], reverse=True)

    print(res)


if __name__ =="__main__":
    main()
