# https://zhuanlan.zhihu.com/p/563844587

from openni import openni2
import numpy as np
import cv2

# 全局变量，用于存储当前的深度图像数据
dpt = None


def mousecallback(event, x, y, flags, param):
    """
    鼠标回调函数，用于处理鼠标事件。
    当用户双击左键时，打印出鼠标所在位置的深度值。

    参数:
    - event: 事件类型。
    - x: 鼠标事件发生的x坐标。
    - y: 鼠标事件发生的y坐标。
    - flags: 事件时的标志（不使用）。
    - param: 传递给回调的参数（不使用）。
    """
    global dpt
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if dpt is not None:
            print(f"深度坐标 ({y}, {x}): {dpt[y, x]}")
        else:
            print("深度数据尚未准备就绪。")


def initialize_camera():
    """
    初始化相机和深度传感器。

    返回:
    - dev: 设备对象。
    - depth_stream: 深度流对象。
    """
    # 初始化OpenNI2库
    openni2.initialize()

    # 打开设备
    dev = openni2.Device.open_any()
    print(f"设备信息: {dev.get_device_info()}")

    # 创建深度流
    depth_stream = dev.create_depth_stream()
    depth_stream.start()

    return dev, depth_stream


def main():
    """
    主函数，执行深度数据的读取和显示。
    """
    global dpt
    # 初始化设备和深度流
    dev, depth_stream = initialize_camera()

    # 设置鼠标回调
    cv2.namedWindow('depth')
    cv2.setMouseCallback('depth', mousecallback)

    try:
        while True:
            # 读取深度帧
            frame = depth_stream.read_frame()
            frame_data = np.array(
                frame.get_buffer_as_triplet()).reshape([480, 640, 2])
            dpt = frame_data[:, :, 0].astype(
                'float32') + frame_data[:, :, 1].astype('float32') * 255

            # 显示深度图
            cv2.imshow('depth', dpt)

            # 按 'q' 键退出循环
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # 停止深度流并关闭设备
        depth_stream.stop()
        dev.close()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
