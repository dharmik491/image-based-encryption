from PIL import Image
import numpy as np
import pickle

import key_generator

def image_encryption(public_key, plain_image):
    """
    This function encrypt the given image using Paillier Cryptosystem.
    """
    
    cipher_image = np.asarray(plain_image)
    shape = cipher_image.shape
    cipher_image = cipher_image.flatten().tolist()
    cipher_image = [key_generator.Encrypt(public_key, pix) for pix in cipher_image]
    
    return np.asarray(cipher_image).reshape(shape)


def image_decryption(public_key, private_key, cipher_image):
    """
    This functions decrypt the encrypted image.

    """

    shape = cipher_image.shape
    plain_image = cipher_image.flatten().tolist()
    plain_image = [key_generator.Decrypt(public_key, private_key, pix) for pix in plain_image]
    plain_image = [pix if pix < 255 else 255 for pix in plain_image]
    plain_image = [pix if pix > 0 else 0 for pix in plain_image]
    
    return Image.fromarray(np.asarray(plain_image).reshape(shape).astype(np.uint8))


def increase_brightness(public_key, cipher_image, factor):
    """
    Function to demonstrate homomorphism
    This function increases the brightness of the encrypted image by a given factor.

    """
    shape = cipher_image.shape
    brightend_image = cipher_image.flatten().tolist()
    brightend_image = [key_generator.homomorphic_add_constant(public_key, pix, factor) for pix in brightend_image]
    
    return np.asarray(brightend_image).reshape(shape)


def show_encrypted_image(cipher_image):
    """
    This function is used to show the encrypted image.
    
    """
    
    for i in range(0,512):
        for j in range(0,512):
            for k in range(0,3):
                cipher_image[i][j][k] = cipher_image[i][j][k]%256

    cipher_image = cipher_image.astype(np.uint8)
    im = Image.fromarray(cipher_image)
    im.show()

    # filename = "encrypted-images/" + filename
    # fstream = open(filename, "wb")
    # pickle.dump(cipher_image, fstream)
    # fstream.close()

