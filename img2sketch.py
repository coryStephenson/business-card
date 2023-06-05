% Thanks to https://github.com/hashABCD/Publications/blob/main/Medium/imagetr_opencv/Convert%20Image%20to%20Sketch.ipynb

% Import libraries
import cv2
import matplotlib.pyplot as plt

% Read photo
img=cv2.imread("photo.jpg")

% Show image using openCV
cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

% Display using Matplotlib
plt.imshow(img)
plt.axis(False)
plt.savefig('temp.png')
plt.show()

% The image is not consistant with the original image
% The reason is CV2 uses BGR color scheme whereas plt uses RGB scheme

% Convert BGR to RGB
plt.imshow(img[:,:,::-1])
plt.axis(False)
plt.savefig('temp.png')
plt.show()

% Convert Image to a Pencil Sketch
def sketch_image(photo, k_size):
    #Read Image
    img=cv2.imread(photo)
    
    # Convert to Grey Image
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img=cv2.bitwise_not(grey_img)
    #invert_img=255-grey_img

    # Blur image
    blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)

    # Invert Blurred Image
    invblur_img=cv2.bitwise_not(blur_img)
    #invblur_img=255-blur_img

    # Sketch Image
    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

    # Save Sketch 
    cv2.imwrite('sketch.png', sketch_img)

    # Display sketch
    cv2.imshow('sketch image',sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#Function call
sketch_image(photo='image_1.png', k_size=7)


