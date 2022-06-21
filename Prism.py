import cv2
import potrace

def main():
    imagePath = input("Image Path: ")
    lowerThreshold = int(input("Lower Threshold: "))
    upperThreshold = int(input("Upper Threshold: "))


    image = cv2.imread(imagePath)
    edges = cv2.Canny(image, lowerThreshold, upperThreshold)

    cv2.imshow('Original', image)
    cv2.imshow('Edge Detection', edges)

    for i in range(len(edges)):
        edges[i][edges[i] > 1] = 1
    bitmap = potrace.Bitmap(edges)
    path = bitmap.trace(2, potrace.TURNPOLICY_MINORITY, 1.0, 1, 0.5)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
