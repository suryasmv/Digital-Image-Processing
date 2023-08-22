import cv2

# Load an image from file
image_path = './images/NewYork.jpeg'  # Replace with the actual path of your image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not open or find the image")
else:
    # Display the image in a window
    cv2.imshow('Image', image)

    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
