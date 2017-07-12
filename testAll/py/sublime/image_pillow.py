from PIL import Image
import matplotlib
# img = Image.open("C:\\Users\\Administrator\\Desktop\\test.webp")
# img = img.copy()
# part1 = img.crop((145, 0, 155, 58))
# img.paste(part1, (0, 58, 10, 116))
# print(img.size)
# img.save("C:\\Users\\Administrator\\Desktop\\123test1.webp", "WEBP")

utlo = "C:\\Users\\Administrator\\Desktop\\ori.webp"
utla = "C:\\Users\\Administrator\\Desktop\\after.webp"
b_after = [[157, 58], [145, 58], [265, 58], [277, 58], [181, 58], [169, 58], [241, 58], [253, 58], [109, 58], [97, 58], [289, 58], [301, 58], [85, 58], [73, 58], [25, 58], [37, 58], [13, 58], [1, 58], [121, 58], [133, 58], [61, 58], [49, 58], [217, 58], [229, 58], [205, 58], [193, 58], [145, 0], [157, 0], [277, 0], [265, 0], [169, 0], [181, 0], [253, 0], [241, 0], [97, 0], [109, 0], [301, 0], [289, 0], [73, 0], [85, 0], [37, 0], [25, 0], [1, 0], [13, 0], [133, 0], [121, 0], [49, 0], [61, 0], [229, 0], [217, 0], [193, 0], [205, 0]]
b_ori = [[157, 58], [145, 58], [265, 58], [277, 58], [181, 58], [169, 58], [241, 58], [253, 58], [109, 58], [97, 58], [289, 58], [301, 58], [85, 58], [73, 58], [25, 58], [37, 58], [13, 58], [1, 58], [121, 58], [133, 58], [61, 58], [49, 58], [217, 58], [229, 58], [205, 58], [193, 58], [145, 0], [157, 0], [277, 0], [265, 0], [169, 0], [181, 0], [253, 0], [241, 0], [97, 0], [109, 0], [301, 0], [289, 0], [73, 0], [85, 0], [37, 0], [25, 0], [1, 0], [13, 0], [133, 0], [121, 0], [49, 0], [61, 0], [229, 0], [217, 0], [193, 0], [205, 0]]

imgo = Image.open(utlo)
imgolast = imgo.copy()
imgoori = imgo.copy()
k = 26

for i in range(0, len(b_ori)):
    t = b_ori[i]
    part1 = imgoori.crop((t[0], t[1], t[0]+10, t[1]+58))
    w = int(i % 26)
    h = int(i / 26)

    imgolast.paste(part1, (w*10, h*58, w*10+10, h*58+58))

box = (0, 0, 260, 116)
part1 = imgolast.crop(box)
part1.save("C:\\Users\\Administrator\\Desktop\\oritest.webp", "WEBP")

imga = Image.open(utla)
imgalast = imga.copy()
imgaori = imga.copy()
k = 26

for i in range(0, len(b_after)):
    t = b_after[i]
    part1 = imgaori.crop((t[0], t[1], t[0]+10, t[1]+58))
    w = int(i % 26)
    h = int(i / 26)

    imgalast.paste(part1, (w*10, h*58, w*10+10, h*58+58))

box = (0, 0, 260, 116)
part1 = imgalast.crop(box)
part1.save("C:\\Users\\Administrator\\Desktop\\aftertest.webp", "WEBP")