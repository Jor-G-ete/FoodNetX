'''
In this assignment, you will create a Deep Learning model to detect whether a meal includes specifics ingredients some users are allergic to. For the sake of simplicity, we will consider a growing amount of user are allergic to tomatoes produced in their countries. We'll try to throw a warning if traces of tomatoes are present in the picture.

You are provided with a training and test sets that are labeled with bounding boxes, and way more items than you need to identify. Feel free to discard the extra information or use it if it can help you.
'''

# add the packages
import yaml, pathlib
import matplotlib.pyplot as plt
from matplotlib import image
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops
import pandas as pd
from PIL import Image

# reset the graph
ops.reset_default_graph
# state the session
# session = tf.Session()
print(tf.__version__)


# functions
def has_tomatos(mdl, path_image):
	'''
	Function which loads a image and the analizes in order to check if it contains tomatoes traces
	:param mdl: Machine Learning model already trained
	:param path_image: The data directory path + name of the image
	:return: True if the image has traces of tomatoes else if it doesn't
	'''

	return True


def checker_images():
	'''
	Dummy function to check if the images can be loaded and transformed into numpy arrays
	also used to draw over them the bounding boxes
	:return: Nothing
	'''
	test_img = '0a16a05e951fea337f9b3260f4db95d3.jpeg'
	img = Image.open(data_path + "assignment_imgs/" + test_img)
	data = np.asarray(img)
	print(data)
	plt.imshow(image.imread(data_path + "assignment_imgs/" + test_img))
	plt.show()


def check_sizes():
	'''
	Function to check the maximun dimensions of a bunch of images
	:return: a tuple which contains height and width
	'''
	return (0,0)


def transform_in_np_arr(image_path):
	'''
	Transform a single image into a numpy array
	:param image_path: path of the image
	:return:
	'''
	image = tf.keras.preprocessing.image.load_img(image_path)
	input_arr = tf.keras.preprocessing.image.img_to_array(image)
	return np.array([input_arr])  # Convert single image to a batch.


def transform_to_tensor_coordinates(heg, wid, bound_box):
	'''
	Function to move the coordinates to the scala used by tensorflow
	:param heg: height of the picture
	:param wid: widht of the picture
	:param bound_box: array of 4 in which its include the dimension of the bounding box
	:return:
	'''
	return [float(i/heg) if idx % 2 == 0 else float(i/wid) for idx, i in enumerate(bound_box)]


if "__main__" == __name__:
	# set directories
	conf_dir = "../Config/"
	conf_file = "conf_deep1.yaml"
	with open(r""+conf_dir+conf_file) as file:
		config_list = yaml.full_load(file)

	data_path = config_list['Data_path']
	images_folder = config_list['Images_folder']
	train_size = config_list['Train_size']
	test_size = config_list['Test_size']
	validation_size = config_list['Validation_size']
	num_channels = config_list['Num_channels']
	batch_size = config_list['Batch_size']
	learning_rate = config_list['Learning_rate']
	evaluation_size = config_list['Evaluation_size']

	# hard-coded variables
	data_file_csv = "label_mapping.csv"
	data_file_json = "img_annotations.json"

	# load the data given
	df_lm = pd.read_csv(data_path+data_file_csv, sep=",")
	# avoid using the frames, due to the different numbers of columns will produce an error
	# use series, then move to dict and we will get our parsed dict
	js_im = pd.read_json(data_path+data_file_json, typ="series").to_dict()

	# load images
	bunch_images = pathlib.Path(data_path+images_folder)
	# count the number of images
	image_count = len(list(bunch_images.glob('*.*')))
	# obtain the dimensions of the images
	img_height = 600
	img_width = 600

	# trial ( First picture )
	first_img = list(js_im.keys())[0]
	first_img_np = transform_in_np_arr(data_path+images_folder+first_img)
	first_img_boxes = [ transform_to_tensor_coordinates(img_height, img_width, i['box']) for i in js_im[first_img]]
	colors = len(js_im[first_img])
	# train_ds = tf.keras.preprocessing.image_dataset_from_directory(data_path+images_folder, validation_split=0.2,
	#                                                               subset="training", seed=123,
	#                                                               image_size=(img_height, img_width), batch_size=batch_size)



	# build the deep learning model

	# test it

	# feed back

	# plots

