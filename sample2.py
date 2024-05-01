# https://blog.csdn.net/weixin_55189321/article/details/131014916

import cv2
import numpy as np
from openni import openni2


def depth2xyz(u, v, depthValue):
    fx = 475.977  # 先前获得的IR_FX
    fy = 475.977  # 先前获得的IR_FY
    cx = 319.206  # 先前获得的IR_cx
    cy = 195.92  # 先前获得的IR_cy

    depth = depthValue * 0.001  # 深度值是单位mm，这里转换成m。

    z = float(depth)
    x = float((u - cx) * z) / fx
    y = float((v - cy) * z) / fy
    # u 是像素点的水平坐标，cx 是结构光相机的光学中心在水平方向上的坐标，z 是深度值（m）
    # fx 是结构光相机的水平焦距，v 是像素点的垂直坐标，cy 是结构光相机的光学中心在垂直方向上的
    # 坐标，fy 是结构光相机的垂直焦距

    result = [x, y, z]
    return result


def mousecallback(event, x, y, flags, param):  # 定义双击鼠标响应事件
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("Clicked on color image:", x, y)

        # Get depth value at the clicked position
        depth_frame = depth_stream.read_frame()
        depth_data = np.array(
            depth_frame.get_buffer_as_uint16()).reshape([480, 640])
        depth_value = depth_data[y, x]

        # Convert depth value to coordinates
        coordinate = depth2xyz(x, y, depth_value)
        if coordinate[0] == 0:
            print("Unable to measure at this point.")
        else:
            print("Depth coordinate:", coordinate)


if __name__ == "__main__":
    openni2.initialize()  # 初始化openni库

    dev = openni2.Device.open_any()  # 获取设备的参数，例如型号
    print(dev.get_device_info())

    depth_stream = dev.create_depth_stream()  # 创建深度流
    depth_stream.start()  # 启动深度流

    cap = cv2.VideoCapture(0)  # 捕捉彩色图像
    cv2.namedWindow('color')  # 命名彩色图像窗口
    cv2.setMouseCallback('color', mousecallback)  # 将双击鼠标响应事件绑定彩色图像窗口

    while True:
        ret, frame = cap.read()
        cv2.imshow('color', frame)

        key = cv2.waitKey(1)
        if int(key) == ord('q'):
            break

    depth_stream.stop()
    dev.close()
    cv2.destroyAllWindows()
