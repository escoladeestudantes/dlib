#python 02_Dlib_validation.py
import dlib

#print(dlib.test_simple_object_detector('mask.xml', "mask.svm"))
print(dlib.test_simple_object_detector('mask_validation.xml', "mask.svm"))
