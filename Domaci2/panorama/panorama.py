import cv2
import easygui
import numpy as np

def panorama(img1, img2):

    img1_gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

    sift = cv2.SIFT.create()

    keypoints1, descriptors1 = sift.detectAndCompute(img2_gray, mask=None)
    keypoints2, descriptors2 = sift.detectAndCompute(img1_gray, mask=None)

    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    
    matches = bf.match(descriptors1, descriptors2)
  
    keypoints1 = np.float32([kp.pt for kp in keypoints1])
    keypoints2 = np.float32([kp.pt for kp in keypoints2])
        
    if len(matches) > 4:
        src_pts = np.float32([keypoints1[m.queryIdx] for m in matches])
        dst_pts = np.float32([keypoints2[m.trainIdx] for m in matches])

        homography, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 4)

    width = img2.shape[1] + img1.shape[1]
    height = img2.shape[0] + img1.shape[0]

    img_final = cv2.warpPerspective(img2, homography, (width, height))
    img_final[0:img1.shape[0], 0:img1.shape[1]] = img1

    cv2.imshow('panorama', img_final)

if __name__=="__main__":
    code1 = easygui.fileopenbox()
    img1 = cv2.imread(code1, 1)
    cv2.imshow('slika1', img1)
    cv2.moveWindow('slika1', 200, 200)

    code2 = easygui.fileopenbox()
    img2 = cv2.imread(code2, 1)
    cv2.imshow('slika2', img2)

    panorama(img1, img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()