# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief: train rnn language model
import os

import tensorflow as tf

import pycorrector.rnn_lm.rnn_lm_config as conf
from pycorrector.rnn_lm.data_reader import process_data, generate_batch
from pycorrector.rnn_lm.rnn_lm_model import rnn_model


def main(_):
    # build vocab and word dict
    data_vector, word_to_int = process_data(conf.train_word_path, conf.word_dict_path)
    # batch data
    batches_inputs, batches_outputs = generate_batch(conf.batch_size, data_vector, word_to_int)
    # placeholder
    input_data = tf.placeholder(tf.int32, [conf.batch_size, None])
    output_targets = tf.placeholder(tf.int32, [conf.batch_size, None])
    # create model
    end_points = rnn_model(model='lstm',
                           input_data=input_data,
                           output_data=output_targets,
                           vocab_size=len(word_to_int),
                           rnn_size=128,
                           num_layers=2,
                           batch_size=conf.batch_size,
                           learning_rate=conf.learning_rate)
    saver = tf.train.Saver(tf.global_variables())
    init_op = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
    # start
    with tf.Session() as sess:
        # init
        sess.run(init_op)

        start_epoch = 0
        checkpoint = tf.train.latest_checkpoint(conf.model_dir)
        if checkpoint:
            saver.restore(sess, checkpoint)
            print("restore from the checkpoint {0}".format(checkpoint))
            start_epoch += int(checkpoint.split('-')[-1])
        print('start training...')
        try:
            for epoch in range(start_epoch, conf.epochs):
                n = 0
                n_chunk = len(data_vector) // conf.batch_size
                for batch in range(n_chunk):
                    loss, _, _, perplexity = sess.run([
                        end_points['total_loss'],
                        end_points['last_state'],
                        end_points['train_op'],
                        end_points['perplexity']
                    ], feed_dict={input_data: batches_inputs[n], output_targets: batches_outputs[n]})
                    n += 1
                    print('Epoch: %d, batch: %d, training loss: %.6f, ppl: %.1f' % (epoch, batch, loss, perplexity))
                if epoch % conf.num_save_epochs == 0:
                    saver.save(sess, os.path.join(conf.model_dir, conf.model_prefix), global_step=epoch)
        except KeyboardInterrupt:
            print('Interrupt manually, try saving checkpoint for now...')
            saver.save(sess, os.path.join(conf.model_dir, conf.model_prefix), global_step=epoch)
            print('Last epoch were saved, next time will start from epoch {}.'.format(epoch))


if __name__ == '__main__':
    tf.app.run()
