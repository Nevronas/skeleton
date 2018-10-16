import argparse

class Parser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="")

        self.parser.add_argument("--path",          default="./",         help="Base path of the project")
        self.parser.add_argument("--model",         default="./model/",   help="Path of the model file")
        self.parser.add_argument("--dataset",       default="./dataset/", help="Path of the dataset")
        self.parser.add_argument("--opt",           default="adam",       help="Optimizers : [sgd, rmsprop, adam]")
        self.parser.add_argument("--learning_rate", default=0.001,        help="Value of Learning Rate",               type=float)
        self.parser.add_argument("--batch_size",    default=50,           help="Batch size",                           type=int)
        self.parser.add_argument("--dropout",       default=0.8,          help="Dropout probab. for pre-final layers", type=float)
        self.parser.add_argument("--max_epochs",    default=100,          help="Maximum number of epochs",             type=int)
        self.parser.add_argument("--patience",      default=2,            help="Patience",                             type=int)
        self.parser.add_argument("--patience_inc",  default=2,            help="Patience increase",                    type=int)
        self.parser.add_argument("--improvement",   default=2,            help="Improvement threshold for patience",   type=int)
        self.parser.add_argument("--save_after",    default=0,            help="Save after epochs",                    type=int)
        self.parser.add_argument("--epoch_freq",    default=1,            help="Epoch frequency",                      type=int)
        self.parser.add_argument("--have_patience", default=False,        help="Patience enabled?",                    type=self.str_to_bool)
        self.parser.add_argument("--debug",         default=False,        help="Debug Mode",                           type=self.str_to_bool)
        self.parser.add_argument("--retrain",       default=False,        help="Retrain",                              type=self.str_to_bool)
        self.parser.add_argument("--load",          default =False,       help="Load model",                           type=self.str_to_bool,)
        

    def str_to_bool(self, text):
        return True if text.lower() == "true" else False

    def get_parser(self):
        return self.parser
