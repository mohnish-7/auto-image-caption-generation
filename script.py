# from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
# import torch
# from PIL import Image

# BASE_DIR = './data'
# WORKING_DIR = '././main'
# output_dir = "vit-gpt-model"

# model = VisionEncoderDecoderModel.from_pretrained(output_dir)
# feature_extractor = ViTImageProcessor.from_pretrained(output_dir)
# tokenizer = AutoTokenizer.from_pretrained(output_dir)

# model.save_pretrained(output_dir)
# feature_extractor.save_pretrained(output_dir)
# tokenizer.save_pretrained(output_dir)

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model.to(device)


# max_length = 16
# num_beams = 4
# gen_kwargs = {"max_length": max_length, "num_beams": num_beams}


# def predict_step(image_paths):
#     images = []
#     for image_path in image_paths:
#         i_image = Image.open(image_path)
#         if i_image.mode != "RGB":
#             i_image = i_image.convert(mode="RGB")

#         images.append(i_image)

#     pixel_values = feature_extractor(
#         images=images, return_tensors="pt").pixel_values
#     pixel_values = pixel_values.to(device)
#     # print(pixel_values)
#     output_ids = model.generate(pixel_values, **gen_kwargs)
#     # print(output_ids)
#     preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
#     preds = [pred.strip() for pred in preds]
#     return preds


# def generate_caption(image_name):
#     # load the image
#     # image_name = "1001773457_577c3a7d70.jpg"
#     image_path = BASE_DIR + '/test/' + image_name
#     cap = predict_step([image_path])
#     image = Image.open(image_path)
#     print(cap[0])
#     return (cap[0])


# def generate_caption_dataset(image_name):
#     # load the image
#     # image_name = "1001773457_577c3a7d70.jpg"
#     image_id = image_name
#     img_path = BASE_DIR + '/Images/' + image_name + '.jpg'
#     image = Image.open(img_path)
#     captions = mapping[image_id]
#     print('\n---------------------Actual---------------------')
#     for caption in captions:
#         print(caption)
#     # predict the caption
#     cap = predict_step([img_path])
#     print('--------------------Predicted--------------------')
#     print(cap[0])


# generate_caption('real_photo_2.jpg')


def text_to_sound(text):
    from playsound import playsound
    import os
    from gtts import gTTS

    myobj = gTTS(text=text, lang='en', tld='com', slow=False)
    myobj.save('audio.mp3')
    playsound('audio.mp3', True)
    os.remove('audio.mp3')
