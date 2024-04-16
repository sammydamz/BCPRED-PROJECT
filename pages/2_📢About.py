import pickle
import streamlit as st
import base64
import xgboost

# Function to convert image to base64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set background image
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

st.set_page_config(
    page_title="About",
)

def main():
    set_background('./images/bgbg.jpg')
    st.markdown(
        """
        <style>
        .header {
            background-color: #540024;
            padding: 10px;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .bodyy {
            background-color: #ffffff;
            padding: 20px;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .bodyy h2 {
            text-align: center;
            font-weight: bold;
            font-size: 2.8rem;
        }
        p {
        text-align: justify;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="bodyy">
         <h2>About Our Breast Tumour Classification Web App</h2>
         <br>
           <p>Our web application is designed to significantly advance the detection and diagnosis of breast cancer by employing advanced machine learning technology to accurately classify breast tumors. This app aims to provide healthcare professionals with a powerful tool that enhances early detection and treatment planning, ultimately improving patient outcomes in the fight against breast cancer.
           </p>
           <p>
           The web app was developed by a team of students from Dapartment of Biomedical Engineering at the  University of Ghana as part of their Introduction to Biomedical Engineering coursework. The team's combined efforts have resulted in a practical application of machine learning technologies in a critical area of healthcare.
           </p>
           The web app was developed by a team of students from Dapartment of Biomedical Engineering at the  University of Ghana as part of their Introduction to Biomedical Engineering coursework. The team's combined efforts have resulted in a practical application of machine learning technologies in a critical area of healthcare.
           <p>
           The dataset for this project was sourced from the comprehensive Wisconsin Breast Cancer Database, which is well-regarded for its detailed and highly reliable dataset of FNA (Fine Needle Aspiration) breast tumor biopsies.
            These samples underwent preprocessing to ensure data integrity and completeness, setting a solid foundation for our predictive model.
           </p>
           <p>
           Initially, the Wisconsin Breast Cancer Database provided ten real-world features, each capturing different aspects of the tumor cells:
            <ol>
            <li>  Radius (mean of distances from the center to points on the perimeter)</li>
            <li>  Texture (standard deviation of gray-scale values)</li>
            <li>  Perimeter</li>
            <li>  Area</li>
            <li>  Smoothness (local variation in radius lengths)</li>
            <li>  Compactness (perimeter^2 / area - 1.0)</li>
            <li>  Concavity (severity of concave portions of the contour)</li>
            <li>  Concave points (number of concave portions of the contour)</li>
            <li>  Symmetry</li>
            <li>  Fractal dimension ("coastline approximation" - 1)</li>
            </ol>
            </p>
            <p>For each of these features, three key measurements were taken: Mean, Standard Error, and the "Worst" or largest (mean of the three largest values).To optimize our model's performance and interpretability, we employed statistical analysis and feature selection. Through this process, we identified the 16 most significant features that held the greatest predictive power. By focusing on these key predictors, we enhanced the efficiency and accuracy of our model.
           </p>
           <p>
           At the heart of our web application lies the XGBoost algorithm. XGBoost which stands for "Extreme Gradient Boosting," is a decision-tree-based ensemble algorithm that utilizes a gradient boosting framework.
           Its  high accuracy and recall make it an ideal choice for real-time prediction tasks, such as classifying breast tumors in our web app.
           By leveraging the power of XGBoost, we can provide healthcare professionals with rapid and reliable predictions, enabling them to make informed decisions and deliver timely interventions.
           </p>
           <br>
           <h2>THE TEAM</h2>
           <div>
            <ul>
                <li><a href="https://www.linkedin.com/in/abena-tiwaa-opoku-boateng" target="_blank">Abena Tiwaa Opoku-Boateng</a></li>
                <li><a href="https://www.linkedin.com/in/stephen-osei-asamoah" target="_blank">Stephen Osei Asamoah</a></li>
                <li><a href="https://www.linkedin.com/in/jessica-konadu-oppong" target="_blank">Jessica Konadu Oppong</a></li>
                <li><a href="https://www.linkedin.com/in/samuel-d-ankapong" target="_blank">Samuel Danquah Ankapong</a></li>
                <li><a href="https://www.linkedin.com/in/ewurama-aidoo" target="_blank">Ewurama Aidoo</a></li>
                <li><a href="https://www.linkedin.com/in/gilbert-nketia" target="_blank">Gilbert Nketia</a></li>
                <li><a href="https://www.linkedin.com/in/maalug-mary-yabia" target="_blank">Maalug Mary Yabia</a></li>
            </ul>
           </div>
        </div>
        """,
        unsafe_allow_html=True
    )
  
if __name__ == "__main__":
    main()
