First, cd into this folder (or the folder containing the folder with your images):
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

Finally, use the following command to convert the COCO fortmat to a TFRecord format:
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