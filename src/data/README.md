Use this command inside current folder when using labelme to get correct label indexing and output folder:

```bash
cd .../root-tip-mitosis-ml/src/data/
labelme images/ --nodata --validatelabel exact --labels labels.txt
```

and use the following command to convert the labelme output json to a COCO format:

```bash
cd .../root-tip-mitosis-ml/src/data/
./labelme2coco.py images dataset-coco --labels labels.txt
```