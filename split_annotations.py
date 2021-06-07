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

#class object names
panel_name = ["panel", "add_panel"]
sign_name = ["sign","other_sign"]
sign_panel_name = ["sign","other_sign","panel", "add_panel"]

km_point_name = ['km_point']
unit_name = ['m','M','km','KM', 'Km','kM', 'Km', 'unit', 'mi']

unreadable_name = ['unreadable_line']
readable_name = ['readable_line']
line_name = ["unreadable_line","readable_line"]


def split_any_class (input_dir, output_dir, classes, action=0):
	'''
	input_dir: files from which the classes will be extracted
	output_dir: the filename for saving the result
	classes : to be extacted
	action: 
			0 : drop, 
			1 : keep,
	'''
	data_paths = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
	for file in data_paths:
		root = ET.parse(input_dir+file).getroot()
		#list to keep the order when removing items
		iterator = list(root.iter("object"))
		for item in iterator:
			obj = item.find("name")
			if (action == 0):
				if (obj.text not in classes):
					root.remove(item)
			elif (action == 1):
				if (obj.text in classes):
					root.remove(item)
		tree = ET.ElementTree(root)
		tree.write(output_dir+file)



def split_readable_line (input_dir, output_dir):
	'''
	input_dir: files from which the classes will be extracted
	output_dir: the filename for saving the result
	'''
	data_paths = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
	for file in data_paths:
		root = ET.parse(input_dir+file).getroot()
		iterator = list(root.iter("object"))
		for item in iterator:
			obj = item.find("name")
			if (obj.text in panel_name+sign_name + km_point_name + unit_name + unreadable_name):
					root.remove(item)
			else: 
				obj.text = "readable_line"
				dup = copy.deepcopy(item)
				root.append(dup)
				root.remove(item)
			
		tree = ET.ElementTree(root)
		tree.write(output_dir+file)


def split_line (input_dir, output_dir):
	'''
	input_dir: files from which the classes will be extracted
	output_dir: the filename for saving the result
	'''
	data_paths = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
	for file in data_paths:
		root = ET.parse(input_dir+file).getroot()
		iterator = list(root.iter("object"))
		for item in iterator:
			obj = item.find("name")
			if (obj.text in panel_name+sign_name + km_point_name + unit_name):
				root.remove(item)
			elif (obj.text not in unreadable_name): 
				obj.text = "readable_line"
				dup = copy.deepcopy(item)
				root.append(dup)
				root.remove(item)
		tree = ET.ElementTree(root)
		tree.write(output_dir+file)

def split_line_into_word (input_dir, output_dir):
	'''
	input_dir: files from which the words will be extracted
	output_dir: the filename for saving the result
	'''
	data_paths = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
	for file in data_paths:
		root = ET.parse(input_dir+file).getroot()
		iterator = list(root.iter("object"))
		for item in iterator:
			obj = item.find("name")
			for word in text.split():
				obj.text = word
				dup = copy.deepcopy(item)
				root.append(dup)
			root.remove(item)

		tree = ET.ElementTree(root)
		tree.write(output_dir+file)



def split_unit (input_dir, output_dir):
	'''
	input_dir: files from which the words will be extracted
	output_dir: the filename for saving the result
	'''
	data_paths = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
	for file in data_paths:
		root = ET.parse(input_dir+file).getroot()
		iterator = list(root.iter("object"))
		for item in iterator:
			obj = item.find("name")
			if (obj.text not in unit_name):
				root.remove(item)
			else: 
				dup = copy.deepcopy(item)
				obj = dup.find("name")
				obj.text = "unit"
				root.append(dup)
			
		tree = ET.ElementTree(root)
		tree.write(output_dir+file)





#Calls
'''
split_any_class (files, panel, panel_name)
split_any_class (files, sign, sign_name)
split_any_class (files, sign_panel, panel_name+sign_name)

split_any_class (files, km_point, km_point_name)

split_any_class (files, unreadable_line, unreadable_name)
split_any_class (files, readable_line, readable_name)
split_any_class (files, line, line_name)

split_any_class (files, words,sign_panel_name+line_name+km_point_name+unit_name, action=1)
'''
split_any_class (files, unit, unit_name)
