from openni import openni2
import numpy as np
import cv2


def initialize_depth_camera():
    openni2.initialize()
    dev = openni2.Device.open_any()
    print(f"设备信息: {dev.get_device_info()}")
    depth_stream = dev.create_depth_stream()
    depth_stream.start()
    return dev, depth_stream


def overlay_images(color_image, depth_image):
    depth_colored = cv2.applyColorMap(cv2.convertScaleAbs(
        depth_image, alpha=0.03), cv2.COLORMAP_JET)
    overlayed_image = cv2.addWeighted(color_image, 0.5, depth_colored, 0.5, 0)
    return overlayed_image


def main():
    dev, depth_stream = initialize_depth_camera()
    cv2.namedWindow('Overlay')

    # 使用OpenCV捕获UVC摄像头的彩色图像
    cap = cv2.VideoCapture(1)  # 0是大多数系统中的默认摄像头索引，可能需要调整

    try:
        while True:
            ret, color_image = cap.read()
            if not ret:
                print("未能从彩色摄像头获取图像")
                break
            
            # 水平翻转彩色图像
            color_image = cv2.flip(color_image, 1)  # 1表示水平翻转

            # 调整彩色图像大小以匹配深度图像的分辨率
            color_image = cv2.resize(color_image, (640, 480))

            depth_frame = depth_stream.read_frame()
            frame_data = np.array(
                depth_frame.get_buffer_as_triplet()).reshape([480, 640, 2])
            depth_image = frame_data[:, :, 0].astype(
                'float32') + frame_data[:, :, 1].astype('float32') * 255

            overlayed_image = overlay_images(color_image, depth_image)
            cv2.imshow('Overlay', overlayed_image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        depth_stream.stop()
        dev.close()
        cv2.destroyAllWindows()
        openni2.unload()


if __name__ == "__main__":
    main()
