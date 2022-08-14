from PIL import Image
import pyheif
import glob


def conv(image_path):
    new_name = image_path.replace('heic', 'png')
    heif_file = pyheif.read(image_path)
    data = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
        )
    data.save(new_name, "PNG")



lst = glob.glob("*.heic")
for l in lst:
    conv(l)