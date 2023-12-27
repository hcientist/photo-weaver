# Photo Weaver

This one time back in the day, I got two pictures blown up to poster size, then cut them into strips (one vertical, one horizontal) and wove them together. It was pretty neat. This program does that digitally. (for the time being it doesn't attempt to create shadow or deformation effects of the paper being bent and woven).

## Usage

You will need the 2 images you'd like to weave together. The resulting image will be the size of the first image.

```python
python  photo_weaver.py -i <image1> <image2> -o <output_image_path>
```

You can optionally change the default size of the weaving. The default is to use column strips of 60 pixels and row strips of 60 pixels. You can either specify 1 value for --region_w_h to use that value for both, or specify 2 values to use the first for the column strip width and the second for the row strip height.

### Use a smaller size but the same for both dimensions (30 pixels):
```python
python  photo_weaver.py -i <image1> <image2> -o <output_image_path> --region_w_h 30
```

### Use different sizes for the column and row strips (e.g. 10 pixels and 200 pixels, respectively):
```python
python  photo_weaver.py -i <image1> <image2> -o <output_image_path> --region_w_h 10 200
``````