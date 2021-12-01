from fastai.vision import *
from fastai.metrics import error_rate

import numpy as np


def run():
    torch.multiprocessing.freeze_support()
    print('loop;')

    x = "/Users/sajeshshrestha/Projects/Final-Year-Project/FastAi/dataset/seg_train"
    path = Path(x)
    #print(path.ls())

    data = ImageDataBunch.from_folder(
            path,
            train='.',
            valid_pct=0.2,
            ds_tfms=get_transforms(),
            size=224,
            num_workers=4,
            ).normalize(imagenet_stats)
    print(data.classes)
    #data.show_batch(3, fig_size=(7,6))

    model = cnn_learner(data, models.resnet34, metrics=error_rate)
    model.fit_one_cycle(2)
    # Export Model
    print("MODEL TO BE EXPORTED")
    model.export("/Users/sajeshshrestha/Projects/Final-Year-Project/model_acc.pkl")
    print("MODEL EXPORTED!!!")
    

if __name__ == '__main__':
    run()
