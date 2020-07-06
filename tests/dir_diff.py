from filecmp import dircmp
import os
import argparse
import easygui
import pandas as pd
from pathlib import Path
import sys
from PyQt5.QtWidgets import (QFileDialog, QAbstractItemView, QListView,
                             QTreeView, QApplication, QDialog)


def convert_bytes(num):
    #this function will convert bytes to MB.. GB.. etc
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return f'{num:.3f} {x}'
        num /= 1024.0

def file_size(file_path):
    #this function will return the file size
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)

def get_files(folder):

	df = pd.DataFrame(columns=['Filename', 'Path', 'Size'])
	for root, dirs, file in os.walk(folder):
		for x in file:
			size = file_size(os.path.join(root, x))
			temp_df = pd.DataFrame([[x, root, size]], columns=['Filename', 'Path', 'Size'])
			df = df.append(temp_df, ignore_index=True)

	return df


class getExistingDirectories(QFileDialog):
    def __init__(self, *args):
        super(getExistingDirectories, self).__init__(*args)
        self.setOption(self.DontUseNativeDialog, True)
        self.setFileMode(self.Directory)
        self.setOption(self.ShowDirsOnly, True)
        self.findChildren(QListView)[0].setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.findChildren(QTreeView)[0].setSelectionMode(QAbstractItemView.ExtendedSelection)

qapp = QApplication(sys.argv)
dlg = getExistingDirectories()
if dlg.exec_() == QDialog.Accepted:
    list_of_folders = dlg.selectedFiles()


df = pd.DataFrame(columns=['Filename', 'Path', 'Size'])
for x in list_of_folders:
	print(x)
	temp_df = get_files(x)
	df = df.append(temp_df, ignore_index=True)

print(df)