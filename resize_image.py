import imageio


if __name__ == '__main__':
    # reader = imageio.get_reader('assets/img/publication_preview/coke-rob.m4v')
    images = imageio.imread('assets/img/publication_preview/ss-quality.png')

    # images = [image[::2, 420:-420:2, :] for i_image, image in enumerate(images) if i_image % 5 == 0]
    images = images[::10, :images.shape[0]:10]
    print(images.shape)
    # images = [imag]
    # images = [image[:, :480, :] for image in images]

    imageio.imsave('assets/img/publication_preview/ss-quality-square.png', images)