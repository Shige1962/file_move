import os, shutil 

#移動したいフォルダにすでに同じファイルがあると上書きされます

print("移動したいファイルのあるパスを入力してください")
print("例: /Users/username/Downloads/")
root_path = input()

print("ファイルの移動先のフォルダのパスを入力してください")
print("例: /Users/username/Documents/")
new_path = input()

print("移動したいファイルの拡張子を入力してください")
print("例: .csv (ドットの入力を忘れずに）")
file_extension = input()

if os.path.exists(root_path) == False:
    print("パスが存在しません")
else: 
    os.chdir(root_path)

for move_filename in os.listdir('.'):
    if not move_filename.endswith(file_extension):
        continue # CSVファイルでなければスキップ ❶
    shutil.move(move_filename, new_path)
    print(move_filename + "は" + new_path + "に移動されました")