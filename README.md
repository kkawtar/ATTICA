# ATTICA: A-new-benchmark-dataset-for-Arabic-Text-based-TraffIC-pAnels-detection

The goal of this dataset is to address  the  lack  of  traffic  panel datasets with Arabic scripts. Our main intention is to provide a  good-quality  dataset  that  will  help  researchers  to  develop robust  AI  approaches  for  traffic  panel  detection  and  Arabic route information extraction. 

Dataset source:

Our  dataset  was  collected  from  open-source  images  on the  internet.  It  includes  a  total  of  1215  images  representing captured roadway scenes from multiple Arabic countries (e.g.Egypt,  Morocco,  Qatar,  Saudi  Arabia,  Algeria).  Images  in our  dataset  include  various  types  of  traffic  signs/panels.

The dataset contains two major sub-datasets:

1-Sign sub-dataset: contains annotations of different types of traffic signs/panels objects. There 5 object categories in this set. Namely: Traffic panel, Traffic sign, Other-sign, Km-point and Add-panel.

2-ext  sub-dataset:  contains  text  objects  with  line  andword level annotations. There two classes of object categories in this set. Namely: Line-level categories (Arabic readable line and Arabic unreable line) and Word-level categories (Arabic word, Arabic digits, Latin digits, special characters and Latin mileage units).

Annotation:

The dataset was annotated using Labelme. This  latter  automatically  generates  XML  metadata  filesaccording to the Pascal VOC format, where it includes the im-age name, size, object bboxes coordinates and correspondingclass  names. 
In  addition,  a  CSV  file  is  provided  to  indicatethe downloadable source links of all images, along with otherinformation  describing  the  contained  traffic  panels  (color,shape, location, type and noise presence).

Dataset download:

To get free access to the dataset for research use, please contact kaoutar.sefriouiboujemaa@usmba.ac.ma
