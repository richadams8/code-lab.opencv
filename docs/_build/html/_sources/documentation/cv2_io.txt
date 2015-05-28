cv2 IO
------------------------


.. automodule:: cv2

    .. function:: imread(filename[, flags])

        `Official OpenCV Documentation <http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html#imread>`_

        :param str filename: The location of the file to open
        :param flags: The flags to use while opening
        :type flags: integer or none
        :return: :class:`numpy.ndarray<numpy:numpy.ndarray>` with the image data in BGR format

    .. function:: imwrite(filename, img[, params])

        `Official OpenCV Documentation <http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html#cv2.imwrite>`_

        :param str filename: The location to save the file to
        :param ndarray img: The image data to write out
        :param params: Format specific save parameters


