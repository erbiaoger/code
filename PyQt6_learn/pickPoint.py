import tensorflow.keras as keras
import tensorflow as tf
import numpy as np


def pickPoint(model, spec, threshold, freq, velo, searchStep=5, returnSpec=False):

    spec = tf.convert_to_tensor(spec)
    spec = tf.expand_dims(spec, -1)
    spec = tf.image.resize(spec, (512, 512))
    spec = tf.expand_dims(spec, 0)
    
    fMax = max(freq)
    fMin = min(freq)
    cMax = max(velo)
    cMin = min(velo)

        
    # CAE Predict
    output = model.predict(spec)
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