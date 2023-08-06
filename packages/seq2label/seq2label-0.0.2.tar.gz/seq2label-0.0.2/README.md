# seq2label

基于 TensorFlow 的通用序列分类算法库。

## 特色
* 通用的序列分类。
* 基于 TensorFlow Estimator: 模型代码很精干，代码量少
* 导出为 `SavedModel` 模型，可以直接使用 TensorFlow Serving 或者 `tf.predictor` API 启动

## TODO
* current [TF Metrics](https://github.com/guillaumegenthial/tf_metrics) is not launch on pypi, but seq2annotation depends on it, so seq2annotation currently can't packaged as python package on pypi

## Credits
- 深受 [Dongjun Lee](https://github.com/DongjunLee) 的 [text-cnn-tensorflow](https://github.com/DongjunLee/text-cnn-tensorflow) 项目的影响