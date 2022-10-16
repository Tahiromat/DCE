import os
import numpy
import streamlit


class UIWidgetsModel:
    def __init__(self):
        pass

    def file_uploader(self):
        return streamlit.file_uploader("Upload an Image", type=["PNG", "JPEG", "JPG"])

    def save_uploded_image(self, image_file, saved_path):
        with open(os.path.join(saved_path, image_file.name), "wb") as f:
            f.write(image_file.getbuffer())

    def create_slider_for_range_of_colors(
        self,
        colors: list[str] = [],
        ranges: list[int] = [],
    ):
        red_value = streamlit.slider(colors[0], 0, ranges[0])
        green_value = streamlit.slider(colors[1], 0, ranges[1])
        blue_value = streamlit.slider(colors[2], 0, ranges[2])
        n_clusters = streamlit.number_input("Insert a number of cluster", min_value=2)
        return red_value, green_value, blue_value, n_clusters

    def create_visual_palette_for_clusters(self, clusters):
        width = 800
        palette = numpy.zeros((100, width, 3), numpy.uint8)

        steps = width / clusters.cluster_centers_.shape[0]
        for idx, centers in enumerate(clusters.cluster_centers_):
            palette[:, int(idx * steps) : (int((idx + 1) * steps)), :] = centers
        return palette
