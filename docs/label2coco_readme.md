# Instance Segmentation Example

## Annotation

```bash
labelme data_annotated --labels labels.txt --nodata --validatelabel exact --config '{shift_auto_shape_color: -2}'
labelme data_annotated --labels labels.txt --nodata --labelflags '{.*: [occluded, truncated], person: [male]}'
```

## Convert to COCO-format Dataset

```bash
# It generates:
#   - data_dataset_coco/JPEGImages
#   - data_dataset_coco/annotations.json
./labelme2coco.py data_annotated data_dataset_coco --labels labels.txt
```
