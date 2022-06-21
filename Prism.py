import cv2
import potrace

def GetPath(edges):
    for i in range(len(edges)):
        edges[i][edges[i] > 1] = 1
    bitmap = potrace.Bitmap(edges)
    path = bitmap.trace(2, potrace.TURNPOLICY_MINORITY, 1.0, 1, 0.5)
    return path

def GetExpressions(path):
    expressions = []

    for curve in path.curves:
        segments = curve.segments
        start = curve.start_point
        for segment in segments:
            x0, y0 = start
            if segment.is_corner:
                x1, y1 = segment.c
                x2, y2 = segment.end_point
                expressions.append('((1-t)%f+t%f,(1-t)%f+t%f)' % (x0, x1, y0, y1))
                expressions.append('((1-t)%f+t%f,(1-t)%f+t%f)' % (x1, x2, y1, y2))
            else:
                x1, y1 = segment.c1
                x2, y2 = segment.c2
                x3, y3 = segment.end_point
                expressions.append('((1-t)((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f))+t((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f)),\
                                     (1-t)((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f))+t((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f)))' % \
                                   (x0, x1, x1, x2, x1, x2, x2, x3, y0, y1, y1, y2, y1, y2, y2, y3))
            start = segment.end_point
    return expressions

def main():
    inputFile  = input("Input file: ")
    outputFile = input("Output file: ")
    lowerThreshold = int(input("Lower Threshold: "))
    upperThreshold = int(input("Upper Threshold: "))


    image = cv2.imread(inputFile)
    edges = cv2.Canny(image, lowerThreshold, upperThreshold)

    path = GetPath(edges)
    expressions = GetExpressions(path)

    with open(outputFile, "w+") as file:
        for expression in expressions:
            file.write(expression)
            file.write('\n')
        file.close()


if __name__ == '__main__':
    main()
