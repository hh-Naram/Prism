import cv2
import potrace
import pyfiglet
import inquirer

def WriteExpressions(file, expressions):
     with open(file, "w+") as file:
            for expression in expressions:
                file.write(expression)
                file.write('\n')


def GetPath(edges):
    for i in range(len(edges)):
        edges[i][edges[i] > 1] = 1
    bitmap = potrace.Bitmap(edges)
    path = bitmap.trace(2, potrace.TURNPOLICY_MINORITY, 1.0, 1, 0.5)
    return path

def ExportExpressions(path):
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
                expressions.append('((1-t)((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f))+t((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f)), (1-t)((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f))+t((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f)))' % \
                                   (x0, x1, x1, x2, x1, x2, x2, x3, y0, y1, y1, y2, y1, y2, y2, y3))
            start = segment.end_point
    return expressions

def ExportDesmos(expressions):
    desmosExpressions = []
    desmosExpressionID = 0

    for expression in expressions:
        desmosExpressionID += 1
        desmosExpressions.append('Calc.setExpression({id: \'graph%d\', latex: \'%s\' })' % (desmosExpressionID, expression))
    return desmosExpressions

def ExportSVG(image, edges):
    height, width, channels = image.shape

    expressions = []
    expressions.append(f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">')
    for edge in edges:
        expressions.append('<path d="M')
        for i in range(len(edge)):
            x, y = edge[i][0]
            expressions.append(f"{x} {y} ")
        expressions.append('" style="stroke:pink"/>')
    expressions.append('</svg>')
    return expressions

def main():
    print(pyfiglet.Figlet(font='chunky').renderText('Prism'))

    inputFile = input(' -> Input File: ')
    lowerThreshold = int(input(' > Lower Threshold: '))
    upperThreshold = int(input(' > Upper Threshold: '))

    image = cv2.imread(inputFile)
    flipped = cv2.flip(image, 0)
    edges = cv2.Canny(flipped, lowerThreshold, upperThreshold)
    path = GetPath(edges)

    questions = [
        inquirer.Checkbox('Exports',
                          message='How do you want to export?',
                          choices=[
                              'Latex Expressions: (output.tex)',
                              'Demos Expressions: (output.js)',
                              'SVG file: (output.svg)',
                          ])
    ]
    answers = inquirer.prompt(questions)

    print('-----------------------------')
    print('Image processed successfully.')

    if 'output.tex' in str(answers):
        WriteExpressions('output.tex', ExportExpressions(path))
    if 'output.js' in str(answers):
        WriteExpressions('output.js', ExportDesmos(ExportExpressions(path)))
    if 'output.svg' in str(answers):
        WriteExpressions('output.svg', ExportSVG(image, edges))

if __name__ == '__main__':
    main()
