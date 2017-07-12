from PIL import Image

ori = Image.open("C:\\Users\\Administrator\\Desktop\\oritest.webp")
after = Image.open("C:\\Users\\Administrator\\Desktop\\aftertest.webp")

(width, height) = ori.size
flag = False

for i in range(0, width):
    for j in range(0, height):
        for x in range(0, 2):
            if abs(ori.getpixel((i, j))[x] - after.getpixel((i, j))[x]) > 50:
                print(i)
                print(j)
                flag = True
                break
        if flag:
            break
    if flag:
        break
