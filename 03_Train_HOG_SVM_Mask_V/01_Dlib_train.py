#python 01_Dlib_train.py

import dlib
options = dlib.simple_object_detector_training_options()
options.add_left_right_image_flips = False
options.num_threads = 4
options.be_verbose = True
options.C = 5
detector = dlib.train_simple_object_detector("./mask.xml", "mask.svm", options)
