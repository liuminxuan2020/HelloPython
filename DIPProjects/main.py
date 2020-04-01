import cv2 as cv

print("数字图像处理")


# 获取图像信息的函数
def get_image_info(image):
    """
    获取图像信息的函数
    :param image:
    :return: null
    """
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)

# 获取视频


src = cv.imread("./Img/timg.jpg")
cv.namedWindow("main", cv.WINDOW_AUTOSIZE)
cv.imshow("main", src)
get_image_info(src)
cv.waitKey()

cv.destroyAllWindows()
# 我是测试内容
# print(src)
