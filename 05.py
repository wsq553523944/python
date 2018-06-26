from PIL import Image
import math
import os

# Suppose we need a resolution not larger than 400*300
target1=400
target2=300


def get_all_pic(start_path):

    list=os.listdir(start_path)
    count=0
    filename=[]
    for pic in list:
        filename.append(start_path+pic)
        count+=1

    print('%s pictures list in the folder'%count)
    return filename




def get_image_pixel(filename):

    img=Image.open(filename)
    imgSize=img.size
    (width,height)=imgSize
    return width,height


def reduce_pixel(width,height):

    if width<height:
        target_height=target1
        target_width =target2
          
    else:
        target_height=target2
        target_width =target1
    
    rate_width =target_width/width
    rate_height=target_height/height

    if rate_width<1 and rate_height<1:

        if rate_width<rate_height:
            temp=rate_width

            new_width=math.floor(temp*width)
            new_height=math.floor(temp*height)

        else:
            temp=rate_height
            new_width=math.floor(temp*width)
            new_height=math.floor(temp*height)

    else:
        new_width=width
        new_height=height

    return new_width,new_height

def reduce_image(filename,new_width,new_height,count,end_path):
    img=Image.open(filename)
    out=img.resize((new_width,new_height))
    out.save('%s%s'%(end_path,count)+'.jpg')


def main():
    start_path='E:/pic/'
    end_path='E:/reduced_pic/'

    if os.path.exists(end_path):
        pass
    else:
        os.mkdir(end_path)

    count=0
    for filename in get_all_pic(start_path):
        count+=1
        image_pixel=get_image_pixel(filename)
        reduced_image_pixel=reduce_pixel(image_pixel[0],image_pixel[1])
        reduce_image(filename,reduced_image_pixel[0],reduced_image_pixel[1],count,end_path)

    print('All reduced picture list in %s'%end_path)
if __name__=='__main__':
    main()