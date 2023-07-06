import tensorflow.keras as keras
import tensorflow as tf
import numpy as np



model_file_DAS = './models/CED_west3.h5'
model_das = keras.models.load_model(model_file_DAS)    # Read Model

#TAG: main
def pickPoint(spec, threshold, freq, velo, searchStep=5, returnSpec=False):
	fMax = max(freq)
	fMin = min(freq)
	cMax = max(velo)
	cMin = min(velo)

# 	Preprocessing
	spec = np.flipud(spec)
	spec = tf.convert_to_tensor(spec)
	spec = tf.expand_dims(spec, -1)
	spec = tf.image.resize(spec, (512, 512))
	spec = tf.expand_dims(spec, 0)
	
#	CAE Predict
	output = model_das.predict(spec)
	output = np.squeeze(output)
	
	if returnSpec:
		return output
#	Grid Search	

	point = []
	for f in range(0, 512, searchStep):
		flag = 0
		for c in range(0, 512):
			if output[c,f] > threshold and flag == 0:
				flag = 1
				begin_c = c
		
			elif flag == 1 and output[c,f] < threshold:
				mid_c = begin_c + (c - begin_c)/2
				point.append([mid_c, f])
				flag = 0
				
	point = np.array(point)
	if len(point) == 0:
		return []
	
	point[:,0] = cMax - point[:,0] * (cMax - cMin)/512
	
	point[:,1] = fMin + point[:,1] * (fMax - fMin)/512
	tmp = point[:,0].copy()
	point[:,0] = point[:,1].copy()
	point[:,1] = tmp
#	del tmp
#	print(point)
	return point
	
	
def modeSuperSeparation(curve, freq, velo):
	
	fMax = np.max(freq)
	fMin = np.min(freq)
	cMax = np.max(velo)
	cMin = np.min(velo)
	curves = curve.copy()
	curves[:, 0] = (curves[:, 0] - fMin) / (fMax - fMin)
	curves[:, 1] = (curves[:, 1] - cMin) / (cMax - cMin)
	curves = tf.expand_dims(curves, -1)
#	curve = tf.expand_dims(curve, 0)
	
	
	mode = model_modeSeparation.predict(curves)

	mode = np.around(mode)
	
	return np.hstack([curve, mode])
	
	
def pickPointPlus(spec, threshold, freq, velo, searchStep=5, returnSpec=False):
	fMax = max(freq)
	fMin = min(freq)
	cMax = max(velo)
	cMin = min(velo)

# 	Preprocessing
	spec = np.flipud(spec)
	spec = tf.convert_to_tensor(spec)
	spec = tf.expand_dims(spec, -1)
	spec = tf.image.resize(spec, (512, 512))
	spec = tf.expand_dims(spec, 0)
	
#	CAE Predict
	output = model_das.predict(spec)
	output = np.squeeze(output)
	
	if np.ndim(output) < 3:
		raise TypeError('The network type Error, the PLUS model is needed!')
		
	outputMode = output[:,:,1]
	output = output[:,:,0]
	
	if returnSpec:
		return output
#	Grid Search	

	point = []
	for f in range(0, 512, searchStep):
		flag = 0
		for c in range(0, 512):
			if output[c,f] > threshold and flag == 0:
				flag = 1
				begin_c = c
		
			elif flag == 1 and output[c,f] < threshold:
				mid_c = begin_c + (c - begin_c)/2
				modeNum =  np.around(5-outputMode[int(mid_c), f])
				if modeNum<1:
					modeNum = 0
				point.append([mid_c, f, modeNum])
				flag = 0
				
	point = np.array(point)
	if len(point) == 0:
		return []
	
	point[:,0] = cMax - point[:,0] * (cMax - cMin)/512
	
	point[:,1] = fMin + point[:,1] * (fMax - fMin)/512
	tmp = point[:,0].copy()
	point[:,0] = point[:,1].copy()
	point[:,1] = tmp
#	del tmp
	print(point)
	return point
	
	
	
		
	
