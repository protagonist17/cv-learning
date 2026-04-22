import cv2  #导入OPENCV库，负责所有图像处理工作
import numpy as np  #导入NUMPY库并给它起个别名叫NP,NP擅长处理“数组”和“二进制数据”

img_path = r'D:/OneDrive/桌面/主角太想进步了/20260422.png'
#把图片的完整路径存到一个变量里，前面的r是原始字符串，告诉PYTHON不要对路径里的\做任何转义处理
# 使用 numpy 从文件读取二进制数据，再用 OpenCV 解码

img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)
#img_data = np.fromfile(img_path, dtype=np.uint8)
#让 numpy 直接去硬盘上把图片文件原封不动地读出来，当成一串“0和1”的字节流，存到 img_data 这个数组里
#dtype=np.uint8 意思是“每个字节都是一个 0~255 的整数”dtype=np.uint8 意思是“每个字节都是一个 0~255 的整数”

if img is None:
    print("❌ 读取失败，请检查路径或文件格式")
else:
    #检查图片是否读取成功，条件判断，错误处理
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 保存时同样使用 imencode 以支持中文路径
    #COLOR_BGR2GRAY 是 OpenCV 内置的转换代码
    #将读取成功的彩色图片 img，转换成灰度图
    cv2.imencode('.png', gray)[1].tofile(r'D:/OneDrive/桌面/主角太想进步了/gray_image.png')
    #cv2.imencode('.png', gray)[1].tofile(...)
    #保存图片的“镜像操作”
    #mencode 把处理好的灰度图 gray 重新编码成 .png 格式的字节流，[1] 是取编码后的数据部分。
    #.tofile(...) 再把这些字节流直接写入硬盘，同样完美支持中文路径
    print("✅ 成功！灰度图已保存")

    #读取或保存带中文路径的图片
    '''
    import cv2
    import numpy as np

    # --- 读取中文路径图片 ---
    img_data = np.fromfile('你的中文路径.png', dtype=np.uint8)
    img = cv2.imdecode(img_data, cv2.IMREAD_COLOR)

    # --- 处理图片（比如转灰度）---
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # --- 保存到中文路径 ---
    cv2.imencode('.png', gray)[1].tofile('你的中文保存路径_gray.png')
    '''
    