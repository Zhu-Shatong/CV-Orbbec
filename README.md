# CV-Orbbec

## 测试摄像头连接

在一切开始之前，如果您是windows系统，请先运行 `SensorDriver_V4.3.0.20`。

打开文件夹 `测试程序-OrbbecViewer` 并且运行。

![示意图](https://cdn.jsdelivr.net/gh/Zhu-Shatong/cloudimg/img/示意图.png)

##  创建虚拟环境与安装相关包

```shell
conda create orbbec python=3.9    
```

```shell
conda activate orbbec 
```

```
pip install requirement.txt
```



> numpy==1.26.4
>
> opencv-python==4.9.0.80
>
> openni==2.3.0



reference：

[关于orbbec gemini rgb-d相机在windows系统中使用Python库Openni调用深度流与RGB图的结合并进行结构光测距_pyorbbecsdk-CSDN博客](https://blog.csdn.net/weixin_55189321/article/details/131014916)

[Orbbec-Astra相机windows系统下Python配置使用 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/563844587)

[奥比中光AI开放平台|全球首个聚焦3D视觉开放平台 (orbbec.com.cn)](https://vcp.developer.orbbec.com.cn/resourceCenter?defaultSelectedKeys=55)



值得注意的是：

我们的摄像头不支持 OrbeccSDK

[pyorbbecsdk奥比中光python版本SDK在Windows下环境配置笔记-CSDN博客](https://blog.csdn.net/m0_70694811/article/details/136344648)

[Error running HelloOrbbec.py SDK sample on Windows10 - Technical Support & Q&A - Orbbec Community Forum (orbbec3d.com)](https://3dclub.orbbec3d.com/t/error-running-helloorbbec-py-sdk-sample-on-windows10/3599/3)

![image-20240501232157341](https://cdn.jsdelivr.net/gh/Zhu-Shatong/cloudimg/img/image-20240501232157341.png)