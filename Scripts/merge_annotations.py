import xml.etree.ElementTree as ET
import os
import re
import copy

#dataset annotation path
files = "..\\voc_annotation_files\\"

#class annotation paths
panel = "..\\voc_annotation_panel\\"
sign = "..\\voc_annotation_sign\\"
sign_panel = "..\\voc_annotation_sign_panel\\"
unreadable_line =  "..\\voc_annotation_unreadable_line\\"
readable_line =  "..\\voc_annotation_readable_line\\"
line =  "..\\voc_annotation_line\\"
words = "..\\voc_annotation_words\\"
text = "..\\voc_annotation_text\\"
unit = "..\\voc_annotation_unit\\"
km_point = "..\\voc_annotation_km_point\\"

def merge_annotation (part_1_dir, part_2_list_dir, out_dir):
	file_data_paths = [f for f in os.listdir(part_1_dir) if os.path.isfile(os.path.join(part_1_dir, f))]

	for file in file_data_paths:
		root = ET.parse(part_1_dir+file).getroot()
		for directory in part_2_list_dir:
			root_directory = ET.parse(directory+file).getroot()
			iterator_directory = list(root_directory.iter("object"))
			for item in iterator_directory:
				dup = copy.deepcopy(item)
				root.append(dup)
						
		tree = ET.ElementTree(root)
		tree.write(out_dir+file)

merge_annotation (words,[line,sign_panel,unit,km_point],files)