import os
import subprocess

NOTEBOOK = "maihopeltonen/nursery-dataset-draft"
SAVE_DIR = "kaggle_notebook"

# Đường dẫn Kaggle CLI (đúng với máy bạn)
KAGGLE_CLI = r"C:\Users\maiho\AppData\Local\Programs\Python\Python313\Scripts\kaggle.exe"

print("📁 Tạo thư mục lưu notebook...")
os.makedirs(SAVE_DIR, exist_ok=True)

print("📥 Đang tải notebook từ Kaggle...")
subprocess.run([KAGGLE_CLI, "kernels", "pull", NOTEBOOK, "-p", SAVE_DIR, "--quiet"], check=True)
print("✅ Tải notebook thành công!")

print("🚀 Đang đẩy notebook lên GitHub...")
subprocess.run(["git", "add", SAVE_DIR + "/"])
subprocess.run(["git", "commit", "-m", "Sync notebook from Kaggle"], check=False)
subprocess.run(["git", "push"], check=True)

print("✅ Hoàn tất! 🎉")
