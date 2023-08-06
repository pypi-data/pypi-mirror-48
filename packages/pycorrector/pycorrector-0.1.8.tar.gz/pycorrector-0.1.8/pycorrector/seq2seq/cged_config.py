# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief: Use CGED corpus
import os

# CGED chinese corpus
raw_train_paths = [
    # '../data/cn/CGED/CGED18_HSK_TrainingSet.xml',
    # '../data/cn/CGED/CGED17_HSK_TrainingSet.xml',
    '../data/cn/CGED/CGED16_HSK_TrainingSet.xml',
    '../data/cn/CGED/sample_HSK_TrainingSet.xml',
]
output_dir = 'output'
# Training data path.
train_path = os.path.join(output_dir, 'train.txt')
# Validation data path.
test_path = os.path.join(output_dir, 'test.txt')

input_vocab_path = os.path.join(output_dir, 'input_vocab.txt')
target_vocab_path = os.path.join(output_dir, 'target_vocab.txt')

# config
batch_size = 128
epochs = 60
rnn_hidden_dim = 256
# Path of the model saved
save_model_path = os.path.join(output_dir, 'cged_seq2seq_model.h5')
encoder_model_path = os.path.join(output_dir, 'cged_seq2seq_encoder.h5')
decoder_model_path = os.path.join(output_dir, 'cged_seq2seq_decoder.h5')

if not os.path.exists(output_dir):
    os.makedirs(output_dir)
