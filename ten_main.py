import tensorflow as tf
#图目录
summary_writer = tf.summary.FileWriter('./chart')
#自定义数据
y=[0.5147,
0.6438,
0.7027,
0.7474]

for i in range(len(y)):
    summary = tf.Summary(value=[
        tf.Summary.Value(tag="accurary", simple_value=y[i]),

    ])
    summary_writer.add_summary(summary, i*30)
summary_writer.close()
