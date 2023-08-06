"""
    HPatches image matching dataset.
"""

import os
import cv2
import numpy as np
# import mxnet as mx
from mxnet.gluon.data import dataset


class HPatches(dataset.Dataset):
    """
    HPatches (full image sequences) image matching dataset.
    Info URL: https://github.com/hpatches/hpatches-dataset
    Data URL: http://icvl.ee.ic.ac.uk/vbalnt/hpatches/hpatches-sequences-release.tar.gz

    Parameters
    ----------
    root : str, default '~/.mxnet/datasets/hpatches'
        Path to the folder stored the dataset.
    mode : str, default 'train'
        'train', 'val', or 'test'.
    alteration : str, default 'all'
        'all', 'i' for illumination or 'v' for viewpoint.
    transform : function, default None
        A function that takes data and label and transforms them.
    """
    def __init__(self,
                 root=os.path.join("~", ".mxnet", "datasets", "hpatches"),
                 mode="train",
                 alteration="all",
                 transform=None):
        super(HPatches, self).__init__()
        assert os.path.exists(root)
        num_images = 5
        image_file_ext = ".ppm"

        self.mode = mode
        self.image_paths = []
        self.warped_image_paths = []
        self.homographies = []

        subdir_names = [name for name in os.listdir(root) if os.path.isdir(os.path.join(root, name))]
        if alteration != "all":
            subdir_names = [name for name in subdir_names if name[0] == alteration]
        for subdir_name in subdir_names:
            subdir_path = os.path.join(root, subdir_name)
            for i in range(num_images):
                k = i + 2
                self.image_paths.append(os.path.join(subdir_path, "1" + image_file_ext))
                self.warped_image_paths.append(os.path.join(subdir_path, str(k) + image_file_ext))
                self.homographies.append(np.loadtxt(os.path.join(subdir_path, "H_1_" + str(k))))

        self._transform = transform

    def __getitem__(self, index):
        image = cv2.imread(self.image_paths[index], flags=cv2.IMREAD_GRAYSCALE)
        warped_image = cv2.imread(self.warped_image_paths[index], flags=cv2.IMREAD_GRAYSCALE)
        homography = self.homographies[index]
        return image, warped_image, homography

    def __len__(self):
        return len(self.image_paths)


def _test():
    dataset = HPatches(
        root="../imgclsmob_data/hpatches",
        mode="train",
        alteration="i",
        transform=None)
    scale_factor = 0.5
    for image, warped_image, _ in dataset:
        cv2.imshow(
            winname="image",
            mat=cv2.resize(
                src=image,
                dsize=None,
                fx=scale_factor,
                fy=scale_factor,
                interpolation=cv2.INTER_NEAREST))
        cv2.imshow(
            winname="warped_image",
            mat=cv2.resize(
                src=warped_image,
                dsize=None,
                fx=scale_factor,
                fy=scale_factor,
                interpolation=cv2.INTER_NEAREST))
        cv2.waitKey(0)
    assert (dataset is not None)


if __name__ == "__main__":
    _test()
