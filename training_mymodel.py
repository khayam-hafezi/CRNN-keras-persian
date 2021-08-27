from keras import backend as K
#from keras.optimizers import Adadelta
from tensorflow.keras.optimizers import Adam, Adadelta, SGD, RMSprop, Adagrad, Adamax, Nadam, Ftrl
from keras.callbacks import EarlyStopping, ModelCheckpoint
from Image_Generator import TextImageGenerator
from parameter import *
K.set_learning_phase(0)
import argparse
import sys
import os
from  loss_optimizer import get_optimizer


# # Model description and training
parser = argparse.ArgumentParser()
parser.add_argument("-pw", "--Previousweight", help="Previous weight file directory",
                    type=str, default="models/weights.best.hdf5")
parser.add_argument("-w", "--weight", help="weight file directory",
                    type=str, default="models/weights.best.hdf5")
parser.add_argument("-p", "--opt", help="optimizer",
                    type=str, default="Adadelta")
parser.add_argument("-m", "--model", help="model",
                    type=str, default="model")
args = parser.parse_args()

if args.model == "model":
    print("model")
    from Model import get_Model
elif args.model == "model_256":
    print("model_256")
    from Model_256 import get_Model
elif args.model == "model_T1":
    print("model_T1")
    from Model_T1 import get_Model


model = get_Model(training=True)
model_path = args.Previousweight
try:
    model.load_weights(model_path)
    print("...Previous weight data...")
except:
    print("...New weight data...")
    pass

train_file_path = './DB/train/'
tiger_train = TextImageGenerator(train_file_path, img_w, img_h, batch_size, downsample_factor)
tiger_train.build_data()

valid_file_path = './DB/validation/'
tiger_val = TextImageGenerator(valid_file_path, img_w, img_h, val_batch_size, downsample_factor)
tiger_val.build_data()

selected_optimizer = get_optimizer(args.opt)
print("selected optimizer: ",  selected_optimizer.__str__())
early_stop = EarlyStopping(monitor='loss', min_delta=0.001, patience=4, mode='min', verbose=1)
# checkpoint = ModelCheckpoint(filepath='LSTM+BN5--{epoch:02d}--{val_loss:.3f}.hdf5', monitor='loss', verbose=1, mode='min', period=1)
filepath= args.weight
print(filepath)
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
# the loss calc occurs elsewhere, so use a dummy lambda func for the loss
model.compile(loss=dict(ctc=lambda y_true, y_pred: y_pred), optimizer=selected_optimizer)

# captures output of softmax so we can decode the output during visualization
model.fit_generator(generator=tiger_train.next_batch(),
                    steps_per_epoch=int(tiger_train.n / batch_size),
                    epochs=500,
                    callbacks=[checkpoint],
                    validation_data=tiger_val.next_batch(),
                    validation_steps=int(tiger_val.n / val_batch_size))
