from fastai import * 
from fastai.vision import * 
from PIL import Image as im
import torchvision.transforms as T

class Predict:
    def __init__(self):
        self.learn = load_learner("","checkpoint-01.pkl")
    def predictHTMLDirect(self, img):
        img_pil = im.open(img)
        img_tensor = T.ToTensor()(img_pil)
        img_fastai = Image(img_tensor)
        pred_class, pred_idx, outputs = self.learn.predict(img_fastai)
        return pred_class