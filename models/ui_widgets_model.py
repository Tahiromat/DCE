import os
import numpy
import streamlit
import matplotlib.pyplot as pyplot


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

    def create_visual_palette_for_clusters(
        self, n_clusters, percentage_and_dominance_list
    ):
        block = numpy.ones((50, 50, 3), dtype="uint")
        pyplot.figure(figsize=(12, 8))
        for i in range(len(percentage_and_dominance_list)):
            pyplot.subplot(1, n_clusters, i + 1)
            # block[:] = percentage_and_dominance_list[i][1][::-1] # bgr mode
            block[:] = percentage_and_dominance_list[i][
                1
            ] # rgb mode
            pyplot.imshow(block)
            pyplot.xticks([])
            pyplot.yticks([])
            pyplot.xlabel(
                str(round(percentage_and_dominance_list[i][0] * 100, 2))
                + "%"
                + "\n"
                + str(percentage_and_dominance_list[i][1])
            )
        streamlit.pyplot(pyplot.show())
