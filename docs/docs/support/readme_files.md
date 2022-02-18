---
layout: default
title: Readme Files
parent: Support
---

# Readme Files
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---
# labelme2coco
## Instance Segmentation Example
{: .no_toc }

### Annotation
{: .no_toc }

```bash
labelme data_annotated --labels labels.txt --nodata --validatelabel exact --config '{shift_auto_shape_color: -2}'
labelme data_annotated --labels labels.txt --nodata --labelflags '{.*: [occluded, truncated], person: [male]}'
```

### Convert to COCO-format Dataset
{: .no_toc }

```bash
# It generates:
#   - data_dataset_coco/JPEGImages
#   - data_dataset_coco/annotations.json
./labelme2coco.py data_annotated data_dataset_coco --labels labels.txt
```

## Source
{: .no_toc }

[https://github.com/wkentaro/labelme/tree/main/examples/instance_segmentation](https://github.com/wkentaro/labelme/tree/main/examples/instance_segmentation)

# create_coco_tf_record
## Example usage:
{: .no_toc }

```bash
    python create_coco_tf_record.py --logtostderr \
      --train_image_dir="${TRAIN_IMAGE_DIR}" \
      --val_image_dir="${VAL_IMAGE_DIR}" \
      --test_image_dir="${TEST_IMAGE_DIR}" \
      --train_annotations_file="${TRAIN_ANNOTATIONS_FILE}" \
      --val_annotations_file="${VAL_ANNOTATIONS_FILE}" \
      --testdev_annotations_file="${TESTDEV_ANNOTATIONS_FILE}" \
      --output_dir="${OUTPUT_DIR}"
```

## Source
{: .no_toc }
[https://github.com/tensorflow/models/tree/master/research/object_detection/dataset_tools](https://github.com/tensorflow/models/tree/master/research/object_detection/dataset_tools)