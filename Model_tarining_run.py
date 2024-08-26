Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================== RESTART: C:/MajorProject/Model_training.py ==================
Traceback (most recent call last):
  File "C:/MajorProject/Model_training.py", line 15, in <module>
    model.fit(train_X, train_Y, epochs=50, batch_size=20)
NameError: name 'train_Y' is not defined. Did you mean: 'train_y'?

================== RESTART: C:/MajorProject/Model_training.py ==================
Epoch 1/50
Traceback (most recent call last):
  File "C:/MajorProject/Model_training.py", line 15, in <module>
    model.fit(train_X, train_Y, epochs=50, batch_size=20)
  File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\utils\traceback_utils.py", line 67, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\tensorflow\python\eager\execute.py", line 54, in quick_execute
    tensors = pywrap_tfe.TFE_Py_Execute(ctx._handle, device_name, op_name,
tensorflow.python.framework.errors_impl.InvalidArgumentError: Graph execution error:

Detected at node 'sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits' defined at (most recent call last):
    File "<string>", line 1, in <module>
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\idlelib\run.py", line 164, in main
      ret = method(*args, **kwargs)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\idlelib\run.py", line 580, in runcode
      exec(code, self.locals)
    File "C:/MajorProject/Model_training.py", line 15, in <module>
      model.fit(train_X, train_Y, epochs=50, batch_size=20)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\utils\traceback_utils.py", line 64, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 1409, in fit
      tmp_logs = self.train_function(iterator)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 1051, in train_function
      return step_function(self, iterator)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 1040, in step_function
      outputs = model.distribute_strategy.run(run_step, args=(data,))
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 1030, in run_step
      outputs = model.train_step(data)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 890, in train_step
      loss = self.compute_loss(x, y, y_pred, sample_weight)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 948, in compute_loss
      return self.compiled_loss(
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\compile_utils.py", line 201, in __call__
      loss_value = loss_obj(y_t, y_p, sample_weight=sw)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\losses.py", line 139, in __call__
      losses = call_fn(y_true, y_pred)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\losses.py", line 243, in call
      return ag_fn(y_true, y_pred, **self._fn_kwargs)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\losses.py", line 1860, in sparse_categorical_crossentropy
      return backend.sparse_categorical_crossentropy(
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\backend.py", line 5238, in sparse_categorical_crossentropy
      res = tf.nn.sparse_softmax_cross_entropy_with_logits(
Node: 'sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits'
Received a label value of 5 which is outside the valid range of [0, 1).  Label values: 5 1 2 4 4 5 4 3 5 2 2 5 1 3 3 4 5 5 1 5
	 [[{{node sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits}}]] [Op:__inference_train_function_564]

====================================================================== RESTART: C:/MajorProject/Model_training.py ======================================================================
Epoch 1/50
Traceback (most recent call last):
  File "C:/MajorProject/Model_training.py", line 15, in <module>
    model.fit(train_X, train_Y, epochs=50, batch_size=20)
  File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\utils\traceback_utils.py", line 67, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\tensorflow\python\eager\execute.py", line 54, in quick_execute
    tensors = pywrap_tfe.TFE_Py_Execute(ctx._handle, device_name, op_name,
tensorflow.python.framework.errors_impl.InvalidArgumentError: Graph execution error:

Detected at node 'sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits' defined at (most recent call last):
    File "<string>", line 1, in <module>
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\idlelib\run.py", line 164, in main
      ret = method(*args, **kwargs)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\idlelib\run.py", line 580, in runcode
      exec(code, self.locals)
    File "C:/MajorProject/Model_training.py", line 15, in <module>
      model.fit(train_X, train_Y, epochs=50, batch_size=20)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\utils\traceback_utils.py", line 64, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 1409, in fit
      tmp_logs = self.train_function(iterator)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 1051, in train_function
      return step_function(self, iterator)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 1040, in step_function
      outputs = model.distribute_strategy.run(run_step, args=(data,))
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 1030, in run_step
      outputs = model.train_step(data)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 890, in train_step
      loss = self.compute_loss(x, y, y_pred, sample_weight)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 948, in compute_loss
      return self.compiled_loss(
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\compile_utils.py", line 201, in __call__
      loss_value = loss_obj(y_t, y_p, sample_weight=sw)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\losses.py", line 139, in __call__
      losses = call_fn(y_true, y_pred)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\losses.py", line 243, in call
      return ag_fn(y_true, y_pred, **self._fn_kwargs)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\losses.py", line 1860, in sparse_categorical_crossentropy
      return backend.sparse_categorical_crossentropy(
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\backend.py", line 5238, in sparse_categorical_crossentropy
      res = tf.nn.sparse_softmax_cross_entropy_with_logits(
Node: 'sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits'
Received a label value of 5 which is outside the valid range of [0, 1).  Label values: 2 3 4 3 3 3 3 3 3 2 2 2 2 4 5 1 2 2 5 1
	 [[{{node sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits}}]] [Op:__inference_train_function_564]

====================================================================== RESTART: C:/MajorProject/Model_training.py ======================================================================
Epoch 1/50
Traceback (most recent call last):
  File "C:/MajorProject/Model_training.py", line 15, in <module>
    model.fit(train_X, train_Y, epochs=50, batch_size=20)
  File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\utils\traceback_utils.py", line 67, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\tensorflow\python\eager\execute.py", line 54, in quick_execute
    tensors = pywrap_tfe.TFE_Py_Execute(ctx._handle, device_name, op_name,
tensorflow.python.framework.errors_impl.InvalidArgumentError: Graph execution error:

Detected at node 'sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits' defined at (most recent call last):
    File "<string>", line 1, in <module>
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\idlelib\run.py", line 164, in main
      ret = method(*args, **kwargs)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\idlelib\run.py", line 580, in runcode
      exec(code, self.locals)
    File "C:/MajorProject/Model_training.py", line 15, in <module>
      model.fit(train_X, train_Y, epochs=50, batch_size=20)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\utils\traceback_utils.py", line 64, in error_handler
      return fn(*args, **kwargs)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 1409, in fit
      tmp_logs = self.train_function(iterator)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 1051, in train_function
      return step_function(self, iterator)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 1040, in step_function
      outputs = model.distribute_strategy.run(run_step, args=(data,))
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 1030, in run_step
      outputs = model.train_step(data)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 890, in train_step
      loss = self.compute_loss(x, y, y_pred, sample_weight)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\training.py", line 948, in compute_loss
      return self.compiled_loss(
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\engine\compile_utils.py", line 201, in __call__
      loss_value = loss_obj(y_t, y_p, sample_weight=sw)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\losses.py", line 139, in __call__
      losses = call_fn(y_true, y_pred)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\losses.py", line 243, in call
      return ag_fn(y_true, y_pred, **self._fn_kwargs)
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\losses.py", line 1860, in sparse_categorical_crossentropy
      return backend.sparse_categorical_crossentropy(
    File "C:\Users\naden\AppData\Local\Programs\Python\Python310\lib\site-packages\keras\backend.py", line 5238, in sparse_categorical_crossentropy
      res = tf.nn.sparse_softmax_cross_entropy_with_logits(
Node: 'sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits'
Received a label value of 5 which is outside the valid range of [0, 5).  Label values: 2 4 2 5 5 2 3 2 5 5 4 2 3 5 5 2 2 3 5 3
	 [[{{node sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits}}]] [Op:__inference_train_function_568]

====================================================================== RESTART: C:/MajorProject/Model_training.py ======================================================================
Epoch 1/50
1/5 [=====>........................] - ETA: 1s - loss: 2.0687 - accuracy: 0.0000e+005/5 [==============================] - 0s 6ms/step - loss: 2.0260 - accuracy: 0.0800
Epoch 2/50
1/5 [=====>........................] - ETA: 0s - loss: 1.9115 - accuracy: 0.10005/5 [==============================] - 0s 5ms/step - loss: 1.9218 - accuracy: 0.0800
Epoch 3/50
1/5 [=====>........................] - ETA: 0s - loss: 1.8408 - accuracy: 0.15005/5 [==============================] - 0s 3ms/step - loss: 1.8337 - accuracy: 0.0700
Epoch 4/50
1/5 [=====>........................] - ETA: 0s - loss: 1.8256 - accuracy: 0.10005/5 [==============================] - 0s 1ms/step - loss: 1.7627 - accuracy: 0.2600
Epoch 5/50
1/5 [=====>........................] - ETA: 0s - loss: 1.7835 - accuracy: 0.15005/5 [==============================] - 0s 3ms/step - loss: 1.6989 - accuracy: 0.2900
Epoch 6/50
1/5 [=====>........................] - ETA: 0s - loss: 1.7446 - accuracy: 0.15005/5 [==============================] - 0s 2ms/step - loss: 1.6516 - accuracy: 0.2900
Epoch 7/50
1/5 [=====>........................] - ETA: 0s - loss: 1.5883 - accuracy: 0.30005/5 [==============================] - 0s 4ms/step - loss: 1.6169 - accuracy: 0.2900
Epoch 8/50
1/5 [=====>........................] - ETA: 0s - loss: 1.6000 - accuracy: 0.30005/5 [==============================] - 0s 4ms/step - loss: 1.5812 - accuracy: 0.2900
Epoch 9/50
1/5 [=====>........................] - ETA: 0s - loss: 1.6164 - accuracy: 0.30005/5 [==============================] - 0s 4ms/step - loss: 1.5503 - accuracy: 0.3000
Epoch 10/50
1/5 [=====>........................] - ETA: 0s - loss: 1.5899 - accuracy: 0.20005/5 [==============================] - 0s 2ms/step - loss: 1.5295 - accuracy: 0.3000
Epoch 11/50
1/5 [=====>........................] - ETA: 0s - loss: 1.4617 - accuracy: 0.20005/5 [==============================] - 0s 3ms/step - loss: 1.5063 - accuracy: 0.3200
Epoch 12/50
1/5 [=====>........................] - ETA: 0s - loss: 1.4856 - accuracy: 0.25005/5 [==============================] - 0s 2ms/step - loss: 1.4859 - accuracy: 0.4000
Epoch 13/50
1/5 [=====>........................] - ETA: 0s - loss: 1.4344 - accuracy: 0.35005/5 [==============================] - 0s 2ms/step - loss: 1.4672 - accuracy: 0.4300
Epoch 14/50
1/5 [=====>........................] - ETA: 0s - loss: 1.4452 - accuracy: 0.60005/5 [==============================] - 0s 3ms/step - loss: 1.4506 - accuracy: 0.4600
Epoch 15/50
1/5 [=====>........................] - ETA: 0s - loss: 1.2026 - accuracy: 0.65005/5 [==============================] - 0s 3ms/step - loss: 1.4382 - accuracy: 0.4800
Epoch 16/50
1/5 [=====>........................] - ETA: 0s - loss: 1.3630 - accuracy: 0.50005/5 [==============================] - 0s 4ms/step - loss: 1.4260 - accuracy: 0.5100
Epoch 17/50
1/5 [=====>........................] - ETA: 0s - loss: 1.3248 - accuracy: 0.60005/5 [==============================] - 0s 1ms/step - loss: 1.4144 - accuracy: 0.5100
Epoch 18/50
1/5 [=====>........................] - ETA: 0s - loss: 1.3438 - accuracy: 0.60005/5 [==============================] - 0s 3ms/step - loss: 1.4030 - accuracy: 0.5400
Epoch 19/50
1/5 [=====>........................] - ETA: 0s - loss: 1.4811 - accuracy: 0.45005/5 [==============================] - 0s 2ms/step - loss: 1.3928 - accuracy: 0.5900
Epoch 20/50
1/5 [=====>........................] - ETA: 0s - loss: 1.4776 - accuracy: 0.40005/5 [==============================] - 0s 2ms/step - loss: 1.3814 - accuracy: 0.6500
Epoch 21/50
1/5 [=====>........................] - ETA: 0s - loss: 1.4003 - accuracy: 0.70005/5 [==============================] - 0s 1ms/step - loss: 1.3733 - accuracy: 0.6600
Epoch 22/50
1/5 [=====>........................] - ETA: 0s - loss: 1.3675 - accuracy: 0.70005/5 [==============================] - 0s 2ms/step - loss: 1.3641 - accuracy: 0.6900
Epoch 23/50
1/5 [=====>........................] - ETA: 0s - loss: 1.3329 - accuracy: 0.60005/5 [==============================] - 0s 3ms/step - loss: 1.3531 - accuracy: 0.7200
Epoch 24/50
1/5 [=====>........................] - ETA: 0s - loss: 1.5151 - accuracy: 0.55005/5 [==============================] - 0s 1ms/step - loss: 1.3439 - accuracy: 0.7100
Epoch 25/50
1/5 [=====>........................] - ETA: 0s - loss: 1.2310 - accuracy: 0.85005/5 [==============================] - 0s 2ms/step - loss: 1.3338 - accuracy: 0.7000
Epoch 26/50
1/5 [=====>........................] - ETA: 0s - loss: 1.1332 - accuracy: 0.85005/5 [==============================] - 0s 2ms/step - loss: 1.3265 - accuracy: 0.6700
Epoch 27/50
1/5 [=====>........................] - ETA: 0s - loss: 1.2831 - accuracy: 0.65005/5 [==============================] - 0s 3ms/step - loss: 1.3164 - accuracy: 0.6700
Epoch 28/50
1/5 [=====>........................] - ETA: 0s - loss: 1.3210 - accuracy: 0.70005/5 [==============================] - 0s 3ms/step - loss: 1.3065 - accuracy: 0.7100
Epoch 29/50
1/5 [=====>........................] - ETA: 0s - loss: 1.0486 - accuracy: 1.00005/5 [==============================] - 0s 1ms/step - loss: 1.2965 - accuracy: 0.7400
Epoch 30/50
1/5 [=====>........................] - ETA: 0s - loss: 1.4986 - accuracy: 0.65005/5 [==============================] - 0s 933us/step - loss: 1.2859 - accuracy: 0.7400
Epoch 31/50
1/5 [=====>........................] - ETA: 0s - loss: 1.3291 - accuracy: 0.75005/5 [==============================] - 0s 1ms/step - loss: 1.2751 - accuracy: 0.7300
Epoch 32/50
1/5 [=====>........................] - ETA: 0s - loss: 1.2985 - accuracy: 0.70005/5 [==============================] - 0s 3ms/step - loss: 1.2666 - accuracy: 0.7500
Epoch 33/50
1/5 [=====>........................] - ETA: 0s - loss: 1.1427 - accuracy: 0.80005/5 [==============================] - 0s 0s/step - loss: 1.2567 - accuracy: 0.7500
Epoch 34/50
1/5 [=====>........................] - ETA: 0s - loss: 1.1643 - accuracy: 0.80005/5 [==============================] - 0s 2ms/step - loss: 1.2477 - accuracy: 0.7500
Epoch 35/50
1/5 [=====>........................] - ETA: 0s - loss: 1.2389 - accuracy: 0.75005/5 [==============================] - 0s 3ms/step - loss: 1.2399 - accuracy: 0.7500
Epoch 36/50
1/5 [=====>........................] - ETA: 0s - loss: 1.2207 - accuracy: 0.80005/5 [==============================] - 0s 5ms/step - loss: 1.2311 - accuracy: 0.7200
Epoch 37/50
1/5 [=====>........................] - ETA: 0s - loss: 1.0782 - accuracy: 0.85005/5 [==============================] - 0s 1ms/step - loss: 1.2219 - accuracy: 0.7500
Epoch 38/50
1/5 [=====>........................] - ETA: 0s - loss: 1.0600 - accuracy: 0.85005/5 [==============================] - 0s 1ms/step - loss: 1.2132 - accuracy: 0.7500
Epoch 39/50
1/5 [=====>........................] - ETA: 0s - loss: 1.1643 - accuracy: 0.80005/5 [==============================] - 0s 2ms/step - loss: 1.2039 - accuracy: 0.7500
Epoch 40/50
1/5 [=====>........................] - ETA: 0s - loss: 1.2470 - accuracy: 0.65005/5 [==============================] - 0s 3ms/step - loss: 1.1956 - accuracy: 0.7500
Epoch 41/50
1/5 [=====>........................] - ETA: 0s - loss: 1.1715 - accuracy: 0.80005/5 [==============================] - 0s 3ms/step - loss: 1.1872 - accuracy: 0.7500
Epoch 42/50
1/5 [=====>........................] - ETA: 0s - loss: 1.1332 - accuracy: 0.80005/5 [==============================] - 0s 3ms/step - loss: 1.1788 - accuracy: 0.7500
Epoch 43/50
1/5 [=====>........................] - ETA: 0s - loss: 1.1171 - accuracy: 0.80005/5 [==============================] - 0s 5ms/step - loss: 1.1705 - accuracy: 0.7500
Epoch 44/50
1/5 [=====>........................] - ETA: 0s - loss: 1.2638 - accuracy: 0.65005/5 [==============================] - 0s 2ms/step - loss: 1.1637 - accuracy: 0.7500
Epoch 45/50
1/5 [=====>........................] - ETA: 0s - loss: 1.2044 - accuracy: 0.65005/5 [==============================] - 0s 633us/step - loss: 1.1543 - accuracy: 0.7700
Epoch 46/50
1/5 [=====>........................] - ETA: 0s - loss: 1.1943 - accuracy: 0.75005/5 [==============================] - 0s 1ms/step - loss: 1.1458 - accuracy: 0.7600
Epoch 47/50
1/5 [=====>........................] - ETA: 0s - loss: 1.1673 - accuracy: 0.70005/5 [==============================] - 0s 3ms/step - loss: 1.1379 - accuracy: 0.7600
Epoch 48/50
1/5 [=====>........................] - ETA: 0s - loss: 0.9926 - accuracy: 0.85005/5 [==============================] - 0s 2ms/step - loss: 1.1301 - accuracy: 0.7600
Epoch 49/50
1/5 [=====>........................] - ETA: 0s - loss: 1.0592 - accuracy: 0.85005/5 [==============================] - 0s 0s/step - loss: 1.1218 - accuracy: 0.7500
Epoch 50/50
1/5 [=====>........................] - ETA: 0s - loss: 1.1529 - accuracy: 0.80005/5 [==============================] - 0s 3ms/step - loss: 1.1141 - accuracy: 0.7500
