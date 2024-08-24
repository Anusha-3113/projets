import cv2
import numpy as np
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

def load_model(model_path):
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(model_path, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    return detection_graph

def load_label_map(label_map_path):
    label_map = label_map_util.load_labelmap(label_map_path)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=90, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)
    return category_index

def detect_objects(image, detection_graph, category_index):
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            image_np_expanded = np.expand_dims(image, axis=0)
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            (boxes, scores, classes, num) = sess.run(
                [boxes, scores, classes, num_detections],
                feed_dict={image_tensor: image_np_expanded}
            )

            vis_util.visualize_boxes_and_labels_on_image_array(
                image,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8
            )

    return image

if __name__ == '__main__':
    # Path to the pre-trained model
    model_path = 'path/to/your/frozen_inference_graph.pb'

    # Path to the label map
    label_map_path = 'path/to/your/label_map.pbtxt'

    # Load the pre-trained model
    detection_graph = load_model(model_path)

    # Load the label map
    category_index = load_label_map(label_map_path)

    # Read the input image
    image_path = 'path/to/your/input_image.jpg'
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Perform object detection
    result_image = detect_objects(image, detection_graph, category_index)

    # Display the result
    cv2.imshow('Object Detection', cv2.cvtColor(result_image, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

