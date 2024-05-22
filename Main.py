import os
from PIL import Image

input_folder = "img"
output_folder = "output"
mask = "mask.png"

#def ApplyMask(img): useless unless auto-cropping is added
#    maskl = Image.open(mask)
#    maskl = maskl.convert("RGBA")
#    img = img.convert("RGBA")
#    imgn = Image.new("RGBA",(3300,2550))
#    imgn.paste(img,mask=maskl)
    # imgn.show() #for debug
#    return imgn

def LayerSep(img,crop,imgName):
    #(75,72,975,600) first one
    print("cropping...")
    imgn = img.crop(crop)
    #imgn.show()
    try:
        imgn.save(os.path.join(output_folder,imgName))
        print("saved:"+str(imgName))
    except FileExistsError:
        try:
            os.remove(os.path.join(output_folder,imgName))
        except PermissionError:
            print("lacks perms. fails!")
            return False
        imgn.save(os.path.join(output_folder,imgName))
        return True
    
def LayersPrep(imgf):
    print("prep")
    p = 1
    img = Image.open(os.path.join(input_folder,imgf))
    while p != 12:
        match p:
            case 1:
                crop = (75,72,975,600) #(left, upper, right, lower)
                LayerSep(img,crop,str(p)+".png")
                p = p + 1
            case 2:
                crop = (1200,72,2100,600) 
                LayerSep(img,crop,str(p)+".png")
                p = p + 1
            case 3:
                crop = (2325,72,3225,600)
                LayerSep(img,crop,str(p)+".png")
                p = p + 1
            case 4:
                crop = (75,700,975,1228)
                LayerSep(img,crop,str(p)+".png")
                p = p + 1
            case 5:
                crop = (1200,700,2100,1228)
                LayerSep(img,crop,str(p)+".png")
                p = p + 1
            case 6:
                crop = (2325,700,3225,1228)
                LayerSep(img,crop,str(p)+".png")
                p = p + 1
            case 7:
                crop = (75,1325,975,1853)
                LayerSep(img,crop,str(p)+".png")
                p = p + 1
            case 8:
                crop = (1200,1325,2100,1853)
                LayerSep(img,crop,str(p)+".png")
                p = p + 1
            case 9:
                crop = (2325,1325,3225,1853)
                LayerSep(img,crop,str(p)+".png")
                p = p + 1
            case 10:
                crop = (75,1945,975,2473)
                LayerSep(img,crop,str(p)+".png")
                p = p + 1
            case 11:
                crop = (1200,1945,2100,2473)
                LayerSep(img,crop,str(p)+".png")
                p = p + 1
            case 12:
                crop = (2325,1945,3225,2473)
                LayerSep(img,crop,str(p)+".png")
                p = p + 1



def main():
    for x in os.listdir(input_folder):
        FName = os.fsdecode(x)
        print(FName)
        LayersPrep(FName)
main()
