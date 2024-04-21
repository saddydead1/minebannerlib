from PIL import Image
import nbts


def createImg(layers: dict):
    new_image = Image.new('RGB', (20, 40), (250, 250, 250))

    # for i in layers:
        # print (i)
        # img = Image.open(layers[i])
        # new_image.paste(img, (0, 0))

    # new_image.save('./helm/temp_flag.jpg', "JPEG")

createImg(
    nbts.getPartsFlag('{BlockEntityTag:{Patterns:[{Color:14,Pattern:"cre"},{Color:4,Pattern:"sku"},{Color:13,Pattern:"flo"},{Color:12,Pattern:"mc"}]}}'))
