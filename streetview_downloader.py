import numpy as np
from PIL import Image
import requests
from os.path import join, isfile, isdir
from os import mkdir

output_dir = 'images'
if not isdir(output_dir):
    mkdir(output_dir)

for cind, city in enumerate(['detroit']):
    locs = np.load('samples_{}.npy'.format(city))
    print(len(locs))
    print(city)
    # place your google api key here
    google_key = 'GOOGLE_API_KEY'
    if not isdir(join(output_dir, city)):
        mkdir(join(output_dir, city))

    for i in range(len(locs)):
        loc = locs[i]
        fname = join(output_dir, city, '_'.join([str(i).zfill(6), str(loc[0]), str(loc[1]), str(loc[2])])+'.jpg')
        if isfile(fname):
            continue
        url = "https://maps.googleapis.com/maps/api/streetview?size=640x480&location={},{}&fov=90&heading={}&pitch=15&key={}".format(loc[1], loc[0], loc[2]+90, google_key)
        print(url)
        try:
            im = Image.open(requests.get(url, stream=True).raw)
            im.save(fname)
        except Exception as e:
            print(e, url)
            pass
    # if i==10:
    #     break