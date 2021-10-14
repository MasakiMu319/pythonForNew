from PIL import Image

pil_im = Image.open('../data/001.jpg')
# pil_im.thumbnail((128, 128), resample=Image.BICUBIC)
# pil_im.save('out.jpg')

box = (1200, 100, 1400, 400)
pil_im.crop(box).save('out.jpg')