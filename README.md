# ATTICA: A-new-benchmark-dataset-for-Arabic-Text-based-TraffIC-pAnels-detection

The goal of this dataset is to address  the  lack  of  traffic  panel datasets with Arabic scripts. Our main intention is to provide a  good-quality  dataset  that  will  help  researchers  to  develop robust  AI  approaches  for  traffic  panel  detection  and  Arabic route information extraction. 

## Dataset overview:

Our  dataset  was  collected  from  open-source  images  on the  internet.  It  includes  a  total  of  1215  images  representing captured roadway scenes from multiple Arabic countries (e.g.Egypt,  Morocco,  Qatar,  Saudi  Arabia,  Algeria).  Images  in our  dataset  include  various  types  of  traffic  signs/panels.

The dataset contains two major sub-datasets:

1-Sign sub-dataset: contains annotations of different types of traffic signs/panels objects. There 5 object categories in this set. Namely: Traffic panel, Traffic sign, Other-sign, Km-point and Add-panel.

2-Text  sub-dataset:  contains  text  objects  with  line  andword level annotations. There two classes of object categories in this set. Namely: Line-level categories (Arabic readable line and Arabic unreable line) and Word-level categories (Arabic word, Arabic digits, Latin digits, special characters and Latin mileage units).

## Annotation:

The dataset was annotated using Labelme. This  latter  automatically  generates  XML  metadata  files according to the Pascal VOC format, where it includes the im-age name, size, object bboxes coordinates and correspondingclass  names.

*"Voc annotation file/Annotations.rar" includes a total of 1215 XML annotation file, including all of the dataset's categories.
*"split_annotations.py" is a python script that allows to split the dataset into seperate annotation folders, where each corresponds to a specific category. 

## Images source links:

A  CSV  file named "Filenames_sourceLinks.csv" is  provided  to  indicate the downloadable source links of all images, along with other information  describing  the  contained  traffic  panels:

*TP-shape: indicates the shapes of the TPs in the corresponding image (1: Rectangular, 2:Arrow, 3:Rock, 4: Circular)

*TP-type: indicates the type of the TP based on its content and the roadway-type (1: City-TP, 2:Highway-TP, 3:Public-facilities)

*TP-color: indicates the TPs colors (1:Blue, 2:green, 3:White, 4:yellow, 5:Orange, 6:Black, 7:Other)

*Noise: indicates if the corresponding image includes any noise (0:Yes, 1:No)

*Resolution: indicates if the corresponding image resolution used in our annotation is the same as it is in the sourceLink (0:No, 1:yes)

PS: This csv file helps to preserve the images copyrights.

## Dataset download:

To get free access to the dataset for research use, please contact kaoutar.sefriouiboujemaa@usmba.ac.ma
