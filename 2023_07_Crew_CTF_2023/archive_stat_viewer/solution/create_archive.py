import os
import stat
import zipfile
import tarfile
import subprocess

filename = input("file name: ")

tf = None
zf = None

basename, ext = os.path.splitext(filename)

# create both if ext is empty
if ext in ["", ".zip"]:
	zf = zipfile.ZipFile(f"{basename}.zip", "w")
if ext in ["", ".tar"]:
	tf = tarfile.open(f"{basename}.tar", "w")


def archive_file(content, archive_path, file_path="./tmpfile"):
	with open(file_path, "w") as f:
		f.write(content)

	if zf is not None:
		info = zipfile.ZipInfo(file_path)
		info.filename = archive_path
		info.external_attr |= os.lstat(file_path).st_mode << 16
		zf.writestr(info, content)

	if tf is not None:
		tar_info = tf.gettarinfo(name=file_path)
		tar_info.name = archive_path
		tf.addfile(tar_info, open(file_path, "rb"))

	os.remove(file_path)

def archive_dir(archive_path, dir_path="./tmpdir"):
	os.makedirs(dir_path, exist_ok=True)

	if zf is not None:
		info = zipfile.ZipInfo(dir_path)
		info.filename = archive_path
		info.external_attr |= os.lstat(dir_path).st_mode << 16
		zf.writestr(info, "hoge")

	if tf is not None:
		tar_info = tf.gettarinfo(name=dir_path)
		tar_info.name = archive_path
		tf.addfile(tar_info)

	os.rmdir(dir_path)

def archive_symlink(link_path, archive_path, file_path="./tmpsymlink"):
	os.symlink(link_path, file_path)

	if zf is not None:
		info = zipfile.ZipInfo(file_path)
		info.filename = archive_path
		info.external_attr |= os.lstat(file_path).st_mode << 16
		zf.writestr(info, link_path)

	if tf is not None:
		tar_info = tf.gettarinfo(name=file_path)
		tar_info.name = archive_path
		tf.addfile(tar_info)
	os.remove(file_path)


def archive_link(link_path, archive_path, file_path="./tmplink"):
	if tf is None:
		return

	src_exists = os.path.exists(link_path)
	if not src_exists:
		with open(link_path, "w") as f:
			f.write("test")

	os.link(link_path, file_path)
	
	# 謎
	tar_info = tf.gettarinfo(name=file_path, arcname=link_path)
	tar_info = tf.gettarinfo(name=file_path)
	tar_info.name = archive_path
	
	tf.addfile(tar_info)
	os.remove(file_path)
	if not src_exists:
		os.remove(link_path)

while 1:
	print("[F/f] file")
	print("[D/d] directory")
	print("[S/s] symlink")
	print("[L/l] hardlink (only tar)")
	choice = input("> ").upper()
	if choice == "F":
		content = input("content: ")
		archive_path = input("archive path: ")
		archive_file(content, archive_path)
	elif choice == "D":
		archive_path = input("archive path: ")
		archive_dir(archive_path)
	elif choice == "S":
		link_path = input("symlink path: ")
		archive_path = input("archive path: ")
		archive_symlink(link_path, archive_path)
	elif choice == "L":
		link_path = input("link path: ")
		archive_path = input("archive path: ")
		archive_link(link_path, archive_path)
	else:
		print("End")
		break

if zf is not None:
	zf.close()
	print(f"--- {basename}.zip")
	subprocess.run(["zipinfo", f"{basename}.zip"])
if tf is not None:
	tf.close()
	print(f"--- {basename}.tar")
	subprocess.run(["tar", "tvf", f"{basename}.tar"])

