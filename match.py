import os
import shutil

# Match the images and labels
img_dir = r"D:\fine-tune-yolo-annotation\YOLO_lowerbody_dataset\images\train"
label_dir = r"D:\fine-tune-yolo-annotation\YOLO_lowerbody_dataset\labels\train"
val_dir = os.path.join(os.path.dirname(img_dir), "validation")

# Create the validation folder (if not exists)
os.makedirs(val_dir, exist_ok=True)

# Get the file names (remove the suffix)
image_names = {os.path.splitext(f)[0] for f in os.listdir(img_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))} # get the image file names...
label_names = {os.path.splitext(f)[0] for f in os.listdir(label_dir) if f.lower().endswith('.txt')}

# Find the images without labels
unlabeled = image_names - label_names
print(f"There are {len(image_names)} images, and {len(unlabeled)} images without corresponding labels.")

# Move the unlabeled images to the validation folder
for name in unlabeled:
    src_path = os.path.join(img_dir, name + ".jpg")
    dst_path = os.path.join(val_dir, name + ".jpg")
    if os.path.exists(src_path):
        shutil.move(src_path, dst_path)

print(f"Moved {len(unlabeled)} unlabeled images to: {val_dir}")
