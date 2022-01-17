import os, glob, shutil
from sklearn.model_selection import train_test_split
from my_utils import split_data, order_test_set, create_generators
from dl_models import streetsigns_model
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import tensorflow as tf


if __name__=='__main__':
    # path_to_data = 'C:\\Users\\Jobin\\Ds\\Datasets\\traffic_sign_recognition\\Train'
    # path_to_save_train = 'C:\\Users\\Jobin\\Ds\\Datasets\\traffic_sign_recognition\\training_data\\train'
    # path_to_save_val = 'C:\\Users\\Jobin\\Ds\\Datasets\\traffic_sign_recognition\\training_data\\val'
    # split_data(path_to_data, path_to_save_train=path_to_save_train, path_to_save_val=path_to_save_val)

    # path_to_images = 'C:\\Users\\Jobin\\Ds\\Datasets\\traffic_sign_recognition\\Test'
    # path_to_csv = 'C:\\Users\\Jobin\\Ds\\Datasets\\traffic_sign_recognition\\Test.csv'
    # order_test_set(path_to_images, path_to_csv)

    path_to_train = 'C:\\Users\\Jobin\\Ds\\Datasets\\traffic_sign_recognition\\training_data\\train'
    path_to_val = 'C:\\Users\\Jobin\\Ds\\Datasets\\traffic_sign_recognition\\training_data\\val'
    path_to_test = 'C:\\Users\\Jobin\\Ds\\Datasets\\traffic_sign_recognition\\Test'
    path_to_save_model = './Models'
    batch_size = 64
    epochs = 15

    train_generator, val_generator, test_generator = create_generators(batch_size, path_to_train, path_to_val, path_to_test)
    nbr_classes = train_generator.num_classes

    TRAIN = False
    TEST = False

    if TRAIN:
        ckpt_saver = ModelCheckpoint(
            path_to_save_model,
            monitor='val_accuracy',
            mode='max',
            save_best_only=True,
            save_freq='epoch',
            verbose=1
        )

        early_stop = EarlyStopping(
            monitor='val_accuracy',
            patience=10,
        )

        model = streetsigns_model(nbr_classes)

        model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

        model.fit(
            train_generator,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=val_generator,
            callbacks=[ckpt_saver, early_stop]
        )

    if TEST:
        model = tf.keras.models.load_model('./Models')
        model.summary()

        print('Evaluating validation set')
        model.evaluate(val_generator)

        print('Evaluating test set')
        model.evaluate(test_generator)