from tensorflow.keras.optimizers import Adam, Adadelta, SGD, RMSprop, Adagrad, Adamax, Nadam, Ftrl


def get_optimizer(opt_str):
    if opt_str == "Adam":
        selected_opt = Adam()
    elif opt_str == "Adadelta":
        selected_opt = Adadelta()
    elif opt_str == "SGD":
        selected_opt = SGD()
    elif opt_str == "RMSprop":
        selected_opt = RMSprop()
    elif opt_str == "Adagrad":
        selected_opt = Adagrad()
    elif opt_str == "Adamax":
        selected_opt = Adamax()
    elif opt_str == "Nadam":
        selected_opt = Nadam()
    elif opt_str == "Ftrl":
        selected_opt = Ftrl()
    else:
        selected_opt = Adadelta()
    return selected_opt

