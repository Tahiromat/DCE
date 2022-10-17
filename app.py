import numpy
import streamlit
import matplotlib.pyplot as plt

streamlit.set_option("deprecation.showPyplotGlobalUse", False)

from models.image_processing_model import ImageProcessingModel
from models.ui_widgets_model import UIWidgetsModel
from models.algorithm_model import AlgorithmModel

streamlit.set_page_config(page_title="DCE", page_icon="home", layout="centered")
hide_streamlit_style = """ <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """
streamlit.markdown(hide_streamlit_style, unsafe_allow_html=True)


def main():

    streamlit.title("Dominant Color Analyser")
    with streamlit.sidebar:
        image_file = UIWidgetsModel().file_uploader()

    if image_file is not None:

        UIWidgetsModel().save_uploded_image(image_file, "saved_images")

        with streamlit.sidebar:
            (
                red_value,
                green_value,
                blue_value,
                n_clusters,
            ) = UIWidgetsModel().create_slider_for_range_of_colors(
                ["Red", "Green", "Blue"], [255, 255, 255]
            )

            streamlit.write(
                "   Red Value:",
                red_value,
                "   Green Value:",
                green_value,
                "Blue Value:",
                blue_value,
                "   Number of Cluster:",
                n_clusters,
            )

        col1, col2 = streamlit.columns(2)

        with col1:
            bgr_image = ImageProcessingModel().load_bgr_image(image_file)
            streamlit.subheader("Original 'B-G-R' Image")
            streamlit.image(bgr_image)

        with col2:
            rgb_image = ImageProcessingModel().load_rgb_image(
                image_file, "saved_images"
            )
            rgb_image = ImageProcessingModel().increase_pixel_values(
                rgb_image, red_value, green_value, blue_value
            )
            streamlit.subheader("New 'R-G-B' Image")
            streamlit.image(rgb_image)

        resized_image = ImageProcessingModel().resize_image(rgb_image, 600, 600)
        flat_img = ImageProcessingModel().reshape_image(resized_image)

        model = AlgorithmModel().create_model(n_clusters=n_clusters)
        cluster_1 = model.fit(flat_img)

        percentage_and_dominance_list = (
            AlgorithmModel().create_zipped_percentage_and_dominance_list(
                cluster_1, flat_img
            )
        )

        UIWidgetsModel().create_visual_palette_for_clusters(
            n_clusters, percentage_and_dominance_list
        )


if __name__ == "__main__":
    main()
