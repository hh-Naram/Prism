import cv2

def main():
    imagePath = input("Image Path: ")
    lowerThreshold = int(input("Lower Threshold: "))
    upperThreshold = int(input("Upper Threshold: "))


    image = cv2.imread(imagePath)
    edges = cv2.Canny(image, lowerThreshold, upperThreshold)

    cv2.imshow('Original', image)
    cv2.imshow('Edge Detection', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
