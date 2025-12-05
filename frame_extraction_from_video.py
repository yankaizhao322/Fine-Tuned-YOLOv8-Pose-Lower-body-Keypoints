import cv2
import os

# === 手动输入视频路径 ===
video_path = input("请输入视频文件路径（例如 .avi）：").strip()
# 去除可能存在的引号（防止直接拖拽文件进终端产生引号）
video_path = video_path.replace('"', '').replace("'", "")

# === 准备输出目录 ===
# 获取文件名（不含扩展名），例如 "PDFE05_1"
base_name = os.path.splitext(os.path.basename(video_path))[0]
output_dir = os.path.join("noneedannotation", base_name)
os.makedirs(output_dir, exist_ok=True)

# === 打开视频 ===
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise IOError(f"无法打开视频文件: {video_path}")

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"\n🎥 正在处理 {base_name}: 帧率 {fps:.2f} FPS, 总帧数 {total_frames}")
print("🚀 开始提取每一帧...")

# === 提取每一帧 ===
current_index = 1  # ✅ 计数器从 1 开始，对应 00001

while True:
    ret, frame = cap.read()
    if not ret:
        break  # 视频结束

    # ✅ 命名格式：PDFE05_1_00001.jpg
    # :05d 表示 5 位数字补零
    frame_name = f"{base_name}_{current_index:05d}.jpg"
    save_path = os.path.join(output_dir, frame_name)
    
    cv2.imwrite(save_path, frame)
    

    current_index += 1

cap.release()
print(f"\n\n✅ 提取完成！共保存 {current_index - 1} 张图片到: {output_dir}")