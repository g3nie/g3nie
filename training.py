import os 
import re
import numpy as np

from pylab import *

gg_label = {
	"taeyeon": 0,
	"jessica": 1,
	"tiffany": 2,
	"yoona": 3
}

FOLDER = "/h/u14/g4/00/g3nie/CSC420/Project/g3nie/data/good/"
SKIP = [".", "..", ".DS_STORE"]


if __name__ == '__main__':
	# Load SVM here
	# clf = pickle.load...

	# Open training_label
	train = np.zeros((80,3 * 1024))
	train_label = np.zeros((80,1))
	r = re.compile('([a-z]*)([0-9]*)\.png')
	training_images = os.listdir(FOLDER)
	i = 0
	for training_image in training_images:
		# Skip these
		if training_image in SKIP:
			continue
		# Always two matches
		matches = r.match(training_image)

		# Open image and flatten
		im = imread(FOLDER + training_image)
		train[i,:1024] = im[:,:,0].flatten()
		train[i,1024:2048] = im[:,:,1].flatten()
		train[i,2048:] = im[:,:,2].flatten()
		# Name
		train_label[i] = gg_label[matches.group(1)]


		i = i + 1

	# Feed to SVM here
