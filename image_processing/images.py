from PIL import Image , ImageFilter

# How to filter any image you want 
# First of all chose any image you want to filter

# Here i disided to filter this image , open the image just like this
reddington_image = Image.open('./images/reddington_image.jpg')
ragnar_lothbrok_image = Image.open('./images/ragnar-lothbrok_image.jpg')

# then we can do alot of things like filter or rotate or resize or else
# Here we will filter our image 
# filtered_image = reddington_image.filter(ImageFilter.SMOOTH)

# Then we will save the changes 
# first prameter name for your image then put the path for the new image and use (png)
# filtered_image.save("AnyNameYouWant.png",'png')
# if you run your code , you will save your image with changes

# You can open new images with the change directly without saving the image
# very simple just write 
# filtered_image.show()

# How to rotate our image ?
# crooked = filtered_image.rotate(180) 
# then open the image 
# crooked.show()

# How to resize your image ?
# resize = filtered_image.resize((300,300))
# resize.show()

# You can change the color of your image by doing this
# convert_img = reddington_image.convert('L')
# convert_img.show()

# You can crop your image 
# box = (100,300,950,800)
# crop_image = ragnar_lothbrok_image.crop(box)
# crop_image.show()

# thumbnail very very useful 
print(ragnar_lothbrok_image.size)
ragnar_lothbrok_image.thumbnail((500,500))
ragnar_lothbrok_image.save('thumbnail.png','png')

# resize_img = ragnar_lothbrok_image.resize((650,400))
# resize_img.save('ragnar.png','png')
# resize_img.show()

# new_img = Image.open('ragnar.png')
# new_img.thumbnail()
# new_img.show()
# print(new_img.size)

# if you want to try any of this code line gust take of the commente