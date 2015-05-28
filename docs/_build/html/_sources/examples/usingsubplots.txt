Using Subplots to Display Multiple cv2 Images
----------------------------------------------

Example of how to use subplots to display multiple images::

    import cv2
    from matplotlib import pyplot as plt

    img_bgr = cv2.imread("../samples/polycom_simple.jpg")
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    plt.figure(1)

    plt.subplot(121)
    plt.imshow(img_bgr)
    plt.axis('off')
    plt.title("Without B&R Channel Swapping")

    plt.subplot(122)
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.title("With B&R Channel Swapping")

    plt.show()
