# EAST_Reimplementation
 Text detection using EAST, compatitble with PaddleOCR

This is a reimplementation of EAST using PaddleOCR text detection.

If you're participating in AI TEMPO RUN 07/2021:

Use **AnnotationConverter.py** to convert multiple annot file into a single file.

After training is done, use **SubmissionConverter.py** to convert predicted result file into submission format.

# Note:
This repo is still under developement, here are the problem which might occure:
* While running **AnnotationConverter.py**: Error "EOF detect in file_[num] in line ... " will be raised. To solve this, simply delete the annot file_[num].
* **AnnotationConverter.py** isn't fully functional, self coding is encouraged.
* Another way to fix error "EOF..." is to remove and then add the annot file to the folder again.
