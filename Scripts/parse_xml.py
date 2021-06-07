import xml.etree.ElementTree as ET
import os



#data path
path = "..\\voc_annotation_files\\"
out_panel = "..\\voc_annotation_panel\\"
out_sign = "..\\voc_annotation_sign\\"
out_invisible_line =  "..\\voc_annotation_invisible_line\\"
out_visible_line =  "..\\voc_annotation_visible_line\\"
out_text = "..\\voc_annotation_text\\"

out_names = [out_panel,out_sign,out_invisible_line,out_visible_line,out_text]

for out in out_names:
    if not os.path.exists(out):
        os.makedirs(out)
    
#j ai remarque il y la classe "corrupted" ??????"

keep_name = ["panel","sign","corrupted"]
data_paths = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


for file in data_paths:
    root = ET.parse(path+file).getroot()
    iterator = root.getiterator("object")

    for item in iterator:

        obj = item.find("name")
        
        if (obj.text not in keep_name ):
            obj.text = "text_line"

    tree = ET.ElementTree(root)
    tree.write(path+out+file)
