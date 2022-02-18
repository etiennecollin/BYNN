First, cd into this folder:
```
cd .../root-tip-mitosis-nn/src/data/
```

For correct label indexing, use following command to launch labelme:
```bash
labelme images/ --nodata --validatelabel exact --labels labels.txt
```

and use the following command to convert the labelme json to a COCO format:
```bash
python ./labelme2coco.py images/ dataset-coco/ --labels labels.txt
```
