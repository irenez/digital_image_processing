import numpy as np
import mahotas as mh
from math import pow

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.cm as cm

img_orig = mh.imread( "T-61_5100_city_orig.png" )
img_noise = mh.imread( "T-61_5100_city_noise.png" )

def mean_square_error( I_o, I_f ):
    # make sure the images are of the same dimensions:
    if not ( I_o.shape[0] == I_f.shape[0] and
        I_o.shape[1] == I_f.shape[1]):
            print "Dimensions didn't match"

    M = I_o.shape[0]
    N = I_o.shape[1]

    mse = 0.0
    for x in xrange(M):
        for y in xrange(N):
            mse += ( pow(I_o[x][y] - I_f[x][y], 2) / (M*N) )

    return mse

x_middle = int( img_noise.shape[0] / 2.0 )
y_middle = int( img_noise.shape[1] / 2.0 )

print y_middle, x_middle

# top left
impulsive_noise = img_noise[0:x_middle,0:y_middle]
impulsive_noise_orig = img_orig[0:x_middle,0:y_middle]

print "impulsive noise:", mean_square_error( impulsive_noise, impulsive_noise_orig )

# top right
impulsive_and_white_noise = img_noise[x_middle:,0:y_middle]
impulsive_and_white_noise_orig = img_orig[x_middle:,0:y_middle]

print "impulsive and white_noise:", mean_square_error( impulsive_and_white_noise, impulsive_and_white_noise_orig )

# bottom left
other_noise = img_noise[0:x_middle,y_middle:]
other_noise_orig = img_orig[0:x_middle,y_middle:]

print "other noise:", mean_square_error( other_noise, other_noise_orig )

# bottom right
gaussian_noise = img_noise[x_middle:,y_middle:]
gaussian_noise_orig = img_orig[x_middle:,y_middle:]

print "gaussian noise:", mean_square_error( gaussian_noise, gaussian_noise_orig )


collection_of_image_parts = [ 
    ("Impulsive Noise", impulsive_noise, impulsive_noise_orig),
    ("Impulsive and White Noise", impulsive_and_white_noise, impulsive_and_white_noise_orig),
    ("Other Noise", other_noise, other_noise_orig),
    ("Gaussian Noise", gaussian_noise, gaussian_noise_orig),
]

for c in collection_of_image_parts:
    fig = plt.figure()
    
    title, n, n_orig = c

    a=fig.add_subplot(1,2,1)

    a.set_title( title )

    imgplot = plt.imshow( n, cmap = cm.Greys_r )
    plt.axis('off') # clear x- and y-axes

    a=fig.add_subplot(1,2,2)
    imgplot = plt.imshow( n_orig, cmap = cm.Greys_r )
    plt.axis('off') # clear x- and y-axes

    plt.show()

