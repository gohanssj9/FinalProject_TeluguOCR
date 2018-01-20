from keras.preprocessing.image import ImageDataGenerator  
from keras.preprocessing.image import array_to_img, img_to_array, load_img
import glob

for i in range(1,685):
    input_path = "FinalProject_TeluguOCR/TeluguDataset/train/"+str(i)+"/"+str(i)+".JPEG"
    output_path = "FinalProject_TeluguOCR/SmallTelugu/test/"+str(i) + "/" + str(i) + 'st.{}.JPEG'  
    count = 39

    gen = ImageDataGenerator(  
        rotation_range=0.1,
        width_shift_range=0.2,
        height_shift_range=0.2,
        zoom_range=0.2,
        horizontal_flip=False
    )

    # load image to array
    image = img_to_array(load_img(input_path))

    # reshape to array rank 4
    image = image.reshape((1,) + image.shape)

    # let's create infinite flow of images
    images_flow = gen.flow(image, batch_size=1)  
    for c, new_images in enumerate(images_flow):  
        # we access only first image because of batch_size=1
        new_image = array_to_img(new_images[0], scale=True)
        new_image.save(output_path.format(c + 1))
        if c >= count:
            break