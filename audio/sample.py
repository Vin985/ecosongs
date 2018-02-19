import cv2
import numpy as np
import scipy.ndimage as ndimage

from analyse.indexes import ACI
from audio.extract import AudioExtract


# Remove single spots from an image
def filter_isolated_cells(array, struct):

    filtered_array = np.copy(array)
    id_regions, num_ids = ndimage.label(filtered_array, structure=struct)
    id_sizes = np.array(ndimage.sum(array, id_regions, range(num_ids + 1)))
    area_mask = (id_sizes == 1)
    filtered_array[area_mask[id_regions]] = 0

    return filtered_array


class Sample(AudioExtract):
    def __init__(self, audio, sr, specgen, start=0, infos=None):
        super().__init__(audio, sr)
        self.start = start
        if infos:
            self.infos = infos
        self.specgen = specgen
        self.spectrogram = None

    def get_spectrogram(self, n_fft=None):
        if not self.spectrogram:
            self.spectrogram = self.specgen.create_spectrogram(self, n_fft)
        return (self.spectrogram)

    def get_ACI(self, time_step=None, unit="seconds"):
        self.ACI = ACI(self.get_spectrogram(), time_step, unit)
        return (self.ACI)

    # Decide if given spectrum shows bird sounds or noise only
    def has_bird(self, imgen, threshold=16):

        # working copy
        #img = self.get_spectrogram().spec.copy()
        # img = imgen.create_composite_part(self.get_spectrogram(),
        #                                   (255, 0, 0)).copy()
        img = imgen.spec2img(self.get_spectrogram().spec, (255, 0, 0))
        img = img.convert('L')
        img = np.asarray(img).copy()
        # STEP 1: Median blur
        #img = cv2.medianBlur(img, 5)
        # cv2.imshow('SPEC', img)
        # cv2.waitKey(-1)

        # STEP 2: Median threshold
        col_median = np.median(img, axis=0, keepdims=True)
        row_median = np.median(img, axis=1, keepdims=True)

        img[img < row_median * 3] = 0
        img[img < col_median * 4] = 0
        img[img > 0] = 1

        # STEP 3: Remove singles
        img = filter_isolated_cells(img, struct=np.ones((3, 3)))

        # STEP 4: Morph Closing
        img = cv2.morphologyEx(img, cv2.MORPH_CLOSE,
                               np.ones((5, 5), np.float32))
        cv2.imshow('SPEC', img)
        cv2.waitKey(-1)
        # STEP 5: Frequency crop
        img = img[128:-16, :]
        cv2.imshow('SPEC', img)
        cv2.waitKey(-1)
        # STEP 6: Count columns and rows with signal
        # (Note: We only use rows with signal as threshold, but columns might come
        # in handy in other scenarios)

        # column has signal?
        col_max = np.max(img, axis=0)
        col_max = ndimage.morphology.binary_dilation(
            col_max, iterations=2).astype(col_max.dtype)
        # cthresh = col_max.sum()

        # row has signal?
        row_max = np.max(img, axis=1)
        row_max = ndimage.morphology.binary_dilation(
            row_max, iterations=2).astype(row_max.dtype)
        rthresh = row_max.sum()

        # final threshold
        thresh = rthresh

        # DBUGB: show?
        # print thresh
        # cv2.imshow('BIRD?', img)
        # cv2.waitKey(-1)

        # STEP 7: Apply threshold (Default = 16)
        bird = True
        if thresh < threshold:
            bird = False

        return bird, thresh
