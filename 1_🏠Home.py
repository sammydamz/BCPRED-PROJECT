import numpy as np
import streamlit as st
import base64
import pickle

st.set_page_config(
    page_title="BCPRED",
)

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

# Loading the saved model
bcpred_model = pickle.load(open('brest_cancer_predXGBOOST.sav', 'rb'))


# Creating a function for Prediction
def bcprediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=np.float64)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = bcpred_model.predict(input_data_reshaped)
    probability = bcpred_model.predict_proba(input_data_reshaped)

    if prediction == 1:
        return 'The tumor is MALIGNANT \n with Confidence Score: {:.6f}'.format(probability[0, 1])
    else:
        return 'The tumor is BENIGN \n with Confidence Score: {:.6f}'.format(probability[0, 1])

def main():
    # Set the background image
    set_background('./images/bgbg.jpg')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(' ')
    with col2:
        st.image("BCPRED5copy.png")
    with col3:
        st.write(' ')
            
    # adding CSS styling
    st.markdown(
        """
        <style>
        .header {
            background-color: #540024;
            padding: 10px;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .header h2 {
            color: white;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # displaying the styled header
    st.markdown(
        """
        <div class="header">
            <h2>Breast Tumor Classification Tool</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("""
    <style>
    .stTextInput label {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True
    )
  
    st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #f58f00;
    color: #ffffff;
}
div.stButton > button:hover {
    background-color: #f56a00;
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)
    st.markdown("""
<style>
.stMarkdown.stSuccess {
    color: black !important; /* Changes text color to black */
    background-color: white !important; /* Changes background color to white */
    opacity: 1 !important; /* Ensures no transparency */
}
</style>
""", unsafe_allow_html=True)
            



    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        textureMean = st.text_input('Texture - Mean')
        areaMean = st.text_input('Area - Mean')
        smoothnessMean = st.text_input('Smoothness - Mean')
        concavityMean = st.text_input('Concavity - Mean')
        symmetryMean = st.text_input('Symmetry - Mean')
        fractal_dimensionMean = st.text_input('Fractal_dimension - Mean')
        
    with col2:
        textureSe = st.text_input('Texture - Standard Error')
        areaSe = st.text_input('Area - Standard Error')
        smoothnessSe = st.text_input('Smoothness - Standard Error')
        concavitySe = st.text_input('Concavity - Standard Error')
        symmetrySe = st.text_input('Symmetry - Standard Error')

    with col3:
        fractalDimensionSe = st.text_input('Fractal_dimension - Worst ')
        smoothnessWorst = st.text_input('Smoothness - Worst')
        concavityWorst = st.text_input('Concavity - Worst')
        symmetryWorst = st.text_input('Symmetry - Worst')
        fractalDimensionWorst = st.text_input('Fractal_dimension - Worst')

    
    
    

    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction
    if st.button('Predict'):
        diagnosis = bcprediction([
            textureMean, areaMean, smoothnessMean, concavityMean, symmetryMean, fractal_dimensionMean,
            textureSe, areaSe, smoothnessSe, concavitySe, symmetrySe, fractalDimensionSe,
            smoothnessWorst, concavityWorst, symmetryWorst, fractalDimensionWorst
        ])

    st.markdown(f"""
        <div class="custom-result">
    {diagnosis}
    </div>""", unsafe_allow_html=True
     )

st.markdown("""
<style>
.custom-result {
    background-color: #f0f0f0; 
    border-radius: 10px; 
    padding: 10px; 
    font-weight: bold; 
    color: black; 
}
</style>
""", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
