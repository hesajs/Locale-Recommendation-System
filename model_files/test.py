import fastai
from fastai.vision import * 


load_model = load_learner("/Users/sajeshshrestha/Projects/Final-Year-Project/", "model_acc_93.pkl")

img = open_image('Dharahara.jpg')
pred_class,pred_idx,outputs = load_model.predict(img)

load_model.predict(img)
label = str(pred_class.obj)
print(label)
