import cv2

# Load the two images from file
image1_path = './images/NewYork.jpeg'
image2_path = './images/SiliconValley.jpg'
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

# Check if the images were loaded successfully
if image1 is None or image2 is None:
    print("Error: Could not open or find one or both of the images")
else:
    # Resize images to have the same height (adjust as needed)
    desired_height = 400
    aspect_ratio = image1.shape[1] / image1.shape[0]
    new_width = int(desired_height * aspect_ratio)
    image1 = cv2.resize(image1, (new_width, desired_height))
    image2 = cv2.resize(image2, (new_width, desired_height))

    # Concatenate images horizontally
    combined_image = cv2.hconcat([image1, image2])

    # Display the combined image in a window
    cv2.imshow('Combined Images', combined_image)

    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
