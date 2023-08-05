import numpy as np
import os.path
import hashlib
import itertools as it
import telluric as tl
from calval.config import cache_dir

max_float_range = np.iinfo(np.uint16).max / (1 << 16)


def asfloat(raster_uint16):
    assert raster_uint16.dtype == np.uint16, 'wrong dtype'
    return raster_uint16.astype(float, out_range=(0, max_float_range))


def uncached_get_tile(url, coords):
    raster = tl.GeoRaster2.open(url)
    tile = raster.get_tile(*coords)
    return tile


class TileCache:
    def __init__(self, folder=os.path.join(cache_dir, 'tiles')):
        self.folder = folder
        if not os.path.isdir(folder):
            os.makedirs(folder)

    def get_tile(self, url, coords):
        hash = hashlib.sha1('{}:{}'.format(url, coords).encode()).hexdigest()
        path = os.path.join(self.folder, hash + '.tif')
        if os.path.isfile(path):
            tile = tl.GeoRaster2.open(path)
        else:
            tile = uncached_get_tile(url, coords)
            tile.save(path)
        return tile


def hires_tile(url, base_coords, zoomlevel=None, get_tile=uncached_get_tile, decode=False):
    """
    Get a tile from url, with footprint computed from `base_coords`, and resolution determined
    by `zoomlevel` (>= `base_coords.z`), possibly higher than 256x256.
    if `decode` specified, uint16 values are converted to floats in [0..1)
    """
    roi = tl.GeoVector.from_xyz(*base_coords)
    if zoomlevel is None:
        zoomlevel = base_coords[-1]
    num_tiles = 2 ** (zoomlevel - base_coords[-1])
    xcoord, ycoord = (num_tiles * x for x in base_coords[:2])
    tiles = []
    for addx, addy in it.product(range(num_tiles), repeat=2):
        tiles.append(get_tile(url, (xcoord + addx, ycoord + addy, zoomlevel)))
    unified = tl.georaster.merge_all(tiles, roi=roi)
    if decode:
        unified = asfloat(unified)
    return unified
