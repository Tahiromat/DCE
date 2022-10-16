import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import cv2
import os

def load_image(image_file):
    img = Image.open(image_file)
    return img


def main():
    
    st.title("Dominant Color Analyser")
    image_file = st.file_uploader("Upload Image", type=["PNG", "JPEG", "JPG"])

    if image_file is not None:

        with open(os.path.join("saved_images", image_file.name), "wb") as f:
            f.write(image_file.getbuffer())

        blue_value = st.slider('Blue', 0, 255,)
        green_value = st.slider('Green', 0, 255,)
        red_value = st.slider('Red', 0, 255,)
        st.write('Blue Value:', blue_value,    '   Green Value:', green_value,    '   Red Value:', red_value)

        img = load_image(image_file)
        

# ###################################################################################################################
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(img)


# ###################################################################################################################



# ###################################################################################################################

        img = cv2.imread("saved_images/" + image_file.name)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        dim = (600, 600)

# ###################################################################################################################
        img_rgb = img.copy()
        r = img_rgb[:,:,0] 
        g = img_rgb[:,:,1] 
        b = img_rgb[:,:,2] 

        # increase the pixel values by 100
        r = r + red_value    
        g = g + green_value    
        b = b + blue_value    

        # if pixel values become > 255, subtract 255 
        cond = r[:, :] > 255
        r[cond] = r[cond] - 255 

        cond = g[:, :] > 255
        g[cond] = g[cond] - 255 

        cond = b[:, :] > 255
        b[cond] = b[cond] - 255 

        # assign the modified channel to image
        img_rgb[:,:,0] = r
        img_rgb[:,:,1] = g 
        img_rgb[:,:,2] = b 

        

        with col2:
            st.image(img_rgb)


# ###################################################################################################################

        # resize image
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        flat_img = np.reshape(img,(-1,3))
        n_clusters = 10
        clt = KMeans(n_clusters=n_clusters, random_state=0)

        def palette(clusters):
            width=800
            palette = np.zeros((100, width, 3), np.uint8)

            dominant_colors = np.array(clt.cluster_centers_,dtype='uint')
            percentages = (np.unique(clt.labels_,return_counts=True)[1])/flat_img.shape[0]
            p_and_c = zip(percentages,dominant_colors)
            p_and_c = sorted(p_and_c,reverse=True)

            steps = width/clusters.cluster_centers_.shape[0]
            for idx, centers in enumerate(clusters.cluster_centers_): 
                palette[:, int(idx*steps):(int((idx+1)*steps)), :] = centers
            return palette
        
        
        clt_1 = clt.fit(flat_img)
        st.image(palette(clt_1))


        dominant_colors = np.array(clt.cluster_centers_,dtype='uint')
        percentages = (np.unique(clt.labels_,return_counts=True)[1])/flat_img.shape[0]
        p_and_c = zip(percentages,dominant_colors)
        p_and_c = sorted(p_and_c,reverse=True)
        st.write(p_and_c[0][0]*100)
        st.write(list(p_and_c[0][1]))


        # for i in range(n_clusters):
        #     plt.subplot(1,n_clusters,i+1)
        #     block[:] = p_and_c[i][1][::-1] # we have done this to convert bgr(opencv) to rgb(matplotlib) 
        #     # plt.imshow(block)
        #     plt.xticks([])
        #     plt.yticks([])
        #     plt.xlabel(str(round(p_and_c[i][0]*100,2))+'%')
        #     st.plotly_chart(block)
       
# ###################################################################################################################



    

if __name__ == "__main__":
    main()



