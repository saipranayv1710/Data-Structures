# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter


Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    segments = sorted(segments, key= lambda x:x[1])  #or
    # segments = sorted(segments, key= lambda x:x.end)
    
    curr_right_end = segments[0].end
    points.append( curr_right_end )
    
    for s in segments:
        if s.start > curr_right_end:
            curr_right_end = s.end
            points.append( curr_right_end )
            
    return points

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')