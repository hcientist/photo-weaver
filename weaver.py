import argparse
from PIL import Image


def weave(a, b, out, region_w_h=[60]):
    try:
        with Image.open(a) as img_a, Image.open(b) as img_b:
            # print(a, img_a.format, f"{img_a.size}x{img_a.mode}")
            # print(b, img_b.format, f"{img_b.size}x{img_b.mode}")
            # print(out)
            # print(region_w_h)
            region = region_w_h
            if len(region_w_h) == 1:
                region = region_w_h * 2  # [60] -> [60, 60]
            region = [int(i) for i in region]
            assert (
                img_a.size[0] > region[0]
                and img_a.size[1] > region[1]
                and img_b.size[0] > region[0]
                and img_b.size[1] > region[1]
            ), "Region size is too big"

            odd_col = region[1]
            for i in range(0, min(img_a.size[0], img_b.size[0]), region[0]):
                for j in range(odd_col, min(img_a.size[1], img_b.size[1]), region[1]*2):
                    box = (i, j, i + region[0], j + region[1])
                    a = img_a.crop(box)
                    b = img_b.crop(box)
                    img_a.paste(b, box)
                odd_col = region[1] if odd_col == 0 else 0

            img_a.save(out)
    except OSError:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
        epilog="Text at the bottom of help",
    )
    parser.add_argument("-i", "--infiles", nargs=2, required=True)
    parser.add_argument("-o", "--outfile", required=True)
    parser.add_argument("-r", "--region_w_h", nargs="+", default=[60])
    args = parser.parse_args()
    weave(args.infiles[0], args.infiles[1], args.outfile, args.region_w_h)
