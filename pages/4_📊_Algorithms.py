import streamlit as st
from PIL import Image



hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
"""

showWarningOnDirectExecution = False
image = Image.open('icons/logo.png')


st.set_page_config(page_title = "Algorithms", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

 
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown(" <br> <br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'>© 2023 </h1>", unsafe_allow_html=True)




st.title("Algorithms📊")
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

all_Datasets = ["Select a Dataset","Cyberbulling Classification Dataset"]
data_choice = st.selectbox("Dataset", all_Datasets)
all_Vectorizers = ["Select a Vectorizer", "TF-IDF"]
vect_choice = st.selectbox("Vectorizer", all_Vectorizers)
all_ML_models = ["Select a Machine Learning Algorithm", "Logistic Regression", "Decision Tree", "Random Forest", "Multinomial Naive Bayes", "Support Vector Machine"]
model_choice = st.selectbox("Machine Learning Algorithm", all_ML_models)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

if data_choice == "Select a Dataset" and vect_choice != "Select a Vectorizer" and model_choice != "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Dataset_**]")
elif data_choice != "Select a Dataset" and vect_choice == "Select a Vectorizer" and model_choice != "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Vectorizer_**]")
elif data_choice != "Select a Dataset" and vect_choice != "Select a Vectorizer" and model_choice == "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Machine Learning Algorithm_**]")
elif data_choice == "Select a Dataset" and vect_choice == "Select a Vectorizer" and model_choice != "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Dataset_** and **_Vectorizer_**]")
elif data_choice == "Select a Dataset" and vect_choice != "Select a Vectorizer" and model_choice == "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Dataset_** and **_Machine Learning Algorithm_**]")
elif data_choice != "Select a Dataset" and vect_choice == "Select a Vectorizer" and model_choice == "Select a Machine Learning Algorithm":
    st.warning(":white[You should select **_Vectorizer_** and **_Machine Learning Algorithm_**]")
else:
    if data_choice == "Cyberbulling Classification Dataset":
    # if token_choice == "Tokenizing":
        if vect_choice == "TF-IDF":
            if model_choice == "Logistic Regression":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_82.34%_**]")
            elif model_choice == "Decision Tree":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_81.06%_**]")
            elif model_choice == "Random Forest":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_83.03%_**]")
            elif model_choice == "Multinomial Naive Bayes":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_67.27%_**]")
            elif model_choice == "Support Vector Machine":
                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader("Evaluation Metrics")
                st.success(":green[Accuracy: **_82.52%_**]")

