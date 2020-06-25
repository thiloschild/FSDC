from filecmp import dircmp
import os
import argparse
def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("-t", "--terminal", action="store_true", required=False,
					help="input in terminal")
	args = vars(ap.parse_args())
	
	
	
	group_A = input('Give the path of the first foldergroup: ')
	group_B = input('Give the path of the second foldergroup: ')
	
	for roota, dirsa, filesa in os.walk(group_A):
		for rootb, dirsb, filesb in os.walk(group_B):
			dc = dircmp(roota, rootb)
			if dc.same_files == []:
				pass
			else:
				print('###################################')
				print('Same File found in : '+roota+' and '+rootb)
				print(dc.same_files)	