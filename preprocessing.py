import cv2

def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    _, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    sharpen_kernel = cv2.filter2D(binary_image, -1, np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]))
    
    preprocessed_image_path = 'preprocessed_image.jpg'
    cv2.imwrite(preprocessed_image_path, sharpen_kernel)
    
    return preprocessed_image_path
