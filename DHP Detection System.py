import streamlit as st
import base64
import disease_detection as dd
from feedback_generation import generate_feedback

# Function to encode the image
def get_base64_of_image(image_file):
    with open(image_file, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path to your image
image_path = r"background.jpg"  # Replace with your image path
encoded_image = get_base64_of_image(image_path)

# Custom CSS with background image
background_image_css = f"""
<style>
.stApp {{
    background-image: url("data:image/jpg;base64,{encoded_image}");
    background-size: 100% auto;
    background-attachment: fixed;
}}
</style>
"""

# Apply the background
st.markdown(background_image_css, unsafe_allow_html=True)

# Custom CSS to center the tabs
tabs_css = """
<style>
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center;
        overflow-x: auto;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
    }

    .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
        height: 0px; 
    }

    .stTabs [data-baseweb="tab"] {
        margin-right: 40px;
        margin-left: 40px;
    }
    
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: rgb(88, 192, 217);
    }
    
    .stTabs [aria-selected="true"] {
        color: rgb(88, 192, 217);
    }
</style>
"""
st.markdown(tabs_css, unsafe_allow_html=True)

title_css = """
<style>
.stTitle {
    alignment: center;
    }
</style>
"""
st.markdown(title_css, unsafe_allow_html=True)

st.title("DHP Detection System")

tabs = st.tabs(["Diabetes", "Heart", "Parkinson"])

diabetes_dict = {
    "pregnancies": None,
    "glucose": None,
    "skin_thickness": None,
    "insulin": None,
    "bmi": None,
    "diabetes_pedigree_function": None,
    "age": None,
    }
heart_disease_dict = {
    "age": None,
    "sex": None,
    "cp": None,
    "trestbps": None,
    "chol": None,
    "fbs": None,
    "restecg": None,
    "thalach": None,
    "exang": None,
    "oldpeak": None,
    "slope": None,
    "ca": None,
    "thal": None,
    }
parkinsons_dict = {
    "MDVP:Fo(Hz)": None,
    "MDVP:Fhi(Hz)": None,
    "MDVP:Flo(Hz)": None,
    "MDVP:Jitter(%)": None,
    "MDVP:Jitter(Abs)": None,
    "MDVP:RAP": None,
    "MDVP:PPQ": None,
    "Jitter:DDP": None,
    "MDVP:Shimmer": None,
    "MDVP:Shimmer(dB)": None,
    "Shimmer:APQ3": None,
    "Shimmer:APQ5": None,
    "MDVP:APQ": None,
    "Shimmer:DDA": None,
    "NHR": None,
    "HNR": None,
    "RPDE": None,
    "DFA": None,
    "spread1": None,
    "spread2": None,
    "D2": None,
    "PPE": None,
    }



with tabs[0]:
    st.header("Diabetes Detection")
    with st.form(key="diabetes_form", enter_to_submit=False):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            diabetes_dict["pregnancies"] = st.number_input("Pregnancies", value=None, help="Number of times pregnant. (This is relevant as pregnancy can influence glucose metabolism and diabetes risk.)")
        
        with col2:
            diabetes_dict["glucose"] = st.number_input("Glucose", value=None, help="Your plasma glucose concentration (in mg/dL) after an oral glucose tolerance test. (This is a primary indicator of blood sugar levels.)")
        
        with col3:
            diabetes_dict["skin_thickness"] = st.number_input("Skin Thickness", value=None, help="Triceps skin fold thickness (in mm). (A measure of subcutaneous fat, which can correlate with insulin resistance.)")
            
        with col1:
            diabetes_dict["insulin"] = st.number_input("Insulin", value=None, help="Your 2-hour serum insulin level (in mu U/ml). (Indicates how much insulin your body produces in response to glucose.)")
        
        with col2:
            diabetes_dict["bmi"] = st.number_input("BMI", value=None, help="Body Mass Index (weight in kg / (height in m)^2). (A key measure of body fat based on height and weight, directly linked to diabetes risk.)")
        
        with col3:
            diabetes_dict["diabetes_pedigree_function"] = st.number_input("Diabetes Pedigree Function", value=None, help="A score that indicates the likelihood of diabetes based on family history and genetic predisposition. (A higher value means a stronger family history of diabetes.)")
        
        with col1:
            diabetes_dict["age"] = st.number_input("Age", value=None, help="Your age in years. (Age is a significant factor in the risk of developing diabetes.)")
        
        diabetes_check_button = st.form_submit_button(label="Perform Diabetes Check")
        try:
            if (diabetes_check_button):
                result = dd.detect_disease(tuple(diabetes_dict.values()), "diabetes")
                ai_feedback = generate_feedback(["diabetes", bool(result)], diabetes_dict)
                if (result == 1):
                    st.error("Result: Diabetic")
                else:
                    st.success("Result: Non-diabetic")
                st.subheader("Personalized Feedback:")
                st.write("(Note: Generated with AI, consult doctor for best advice!)")
                st.write(ai_feedback)
        except ValueError:
            st.warning("Invalid values! Either empty or too large! Please input all the fields with proper values!")

with tabs[1]:
    st.header("Heart Disease Detection")
    with st.form(key="heart_disease_form", enter_to_submit=False):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            heart_disease_dict["age"] = st.number_input("Age", value=None, help="Your age in years.")
        
        with col2:
            heart_disease_dict["sex"] = st.number_input("Sex (1-Male, 0-Female)", value=None, help="Your biological sex (1 for male, 0 for female).")
        
        with col3:
            heart_disease_dict["cp"] = st.number_input("Chest Pain Type (0, 1, 2 or 3)", value=None, help="The type of chest pain experienced. (Typically categories like typical angina, atypical angina, non-anginal pain, asymptomatic.)")
            
        with col1:
            heart_disease_dict["trestbps"] = st.number_input("Resting Blood Pressure", value=None, help="Your blood pressure measured at rest (in mmHg).")
        
        with col2:
            heart_disease_dict["chol"] = st.number_input("Serum Cholestoral (in mg/dl)", value=None, help="Your cholesterol level in milligrams per deciliter.")
        
        with col3:
            heart_disease_dict["fbs"] = st.number_input("Fasting Blood Sugar (1-True, 0-False)", value=None, help="Your blood sugar level after fasting. (1 if > 120 mg/dl, 0 otherwise).")
        
        with col1:
            heart_disease_dict["restecg"] = st.number_input("Resting Electrocardiographic Results", value=None, help="Results of your resting electrocardiogram. (Categories indicating normal, ST-T wave abnormality, or left ventricular hypertrophy).")
        
        with col2:
            heart_disease_dict["thalach"] = st.number_input("Maximum Heart Rate Achieved", value=None, help="The highest heart rate reached during exercise.")
        
        with col3:
            heart_disease_dict["exang"] = st.number_input("Exercise Induced Angina (1-Yes, 0-No)", value=None, help="Whether exercise caused chest pain (1 for yes, 0 for no).")
        
        with col1:
            heart_disease_dict["oldpeak"] = st.number_input("Oldpeak", value=None, help="ST depression induced by exercise relative to rest. (Indicates how much the heart's electrical activity changes during exercise).")
        
        with col2:
            heart_disease_dict["slope"] = st.number_input("Slope of The Peak Exercise", value=None, help="The slope of the peak exercise ST segment. (Indicates the trend of the ST segment during the exercise test).")
        
        with col3:
            heart_disease_dict["ca"] = st.number_input("Number of Major Vessels (0-3) colored by flourosopy", value=None, help="The number of major blood vessels observed during a fluoroscopy procedure.")
        
        with col1:
            heart_disease_dict["thal"] = st.number_input("Thal (0-normal; 1-fixed defect; 2-reversable defect)", value=None, help="Results of a Thallium stress test. (Indicates blood flow to the heart: normal, fixed defect, or reversible defect).")
        heart_check_button = st.form_submit_button(label="Perform Heart Disease Check")
        try:
            if (heart_check_button):
                result = dd.detect_disease(tuple(heart_disease_dict.values()), "heart_disease")
                ai_feedback = generate_feedback(["heart disease", bool(result)], heart_disease_dict)
                if (result == 1):
                    st.error("Result: Has a Heart disease")
                else:
                    st.success("Result: No Heart disease")
                st.subheader("Personalized Feedback:")
                st.write("(Note: Generated with AI, consult doctor for best advice!)")
                st.write(ai_feedback)
        except ValueError:
            st.warning("Invalid values! Either empty or too large! Please input all the fields with proper values!")

with tabs[2]:
    st.header("Parkinsons Detection")
    with st.form(key="parkinsons_form", enter_to_submit=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            parkinsons_dict["MDVP:Fo(Hz)"] = st.number_input("MDVP:Fo(Hz)", format="%.5f", value=None, help="Average Vocal Pitch (Hz): The average frequency of your voice's vibration during speech.")
        
        with col2:
            parkinsons_dict["MDVP:Fhi(Hz)"] = st.number_input("MDVP:Fhi(Hz)", format="%.5f", value=None, help="Maximum Vocal Pitch (Hz): The highest frequency your voice reached during the recording.")
        
        with col3:
            parkinsons_dict["MDVP:Flo(Hz)"] = st.number_input("MDVP:Flo(Hz)", format="%.5f", value=None, help="Minimum Vocal Pitch (Hz): The lowest frequency your voice reached during the recording.")
            
        with col1:
            parkinsons_dict["MDVP:Jitter(%)"] = st.number_input("MDVP:Jitter(%)", format="%.5f", value=None, help="Jitter (Percentage): A measure of the percentage variation in your vocal pitch from one cycle to the next. High jitter indicates instability.")
        
        with col2:
            parkinsons_dict["MDVP:Jitter(Abs)"] = st.number_input("MDVP:Jitter(Abs)", format="%.5f", value=None, help="Jitter (Absolute): The absolute average variation in your vocal pitch, measured in microseconds.")
        
        with col3:
            parkinsons_dict["MDVP:RAP"] = st.number_input("MDVP:RAP", format="%.5f", value=None, help="Relative Average Perturbation (RAP): A specific measure of short-term pitch variation (jitter), highlighting voice instability.")
        
        with col1:
            parkinsons_dict["MDVP:PPQ"] = st.number_input("MDVP:PPQ", format="%.5f", value=None, help="Five-point Period Perturbation Quotient (PPQ): Another measure of short-term pitch variation across five vocal cycles.")
        
        with col2:
            parkinsons_dict["Jitter:DDP"] = st.number_input("Jitter:DDP", format="%.5f", value=None, help="A measure of the average difference between consecutive differences in vocal pitch periods.")
        
        with col3:
            parkinsons_dict["MDVP:Shimmer"] = st.number_input("MDVP:Shimmer", format="%.5f", value=None, help="Shimmer (Percentage): A measure of the percentage variation in your vocal amplitude (loudness) from one cycle to the next. High shimmer indicates instability.")
        
        with col1:
            parkinsons_dict["MDVP:Shimmer(dB)"] = st.number_input("MDVP:Shimmer(dB)", format="%.5f", value=None, help="Shimmer (dB): The average absolute variation in vocal amplitude, measured in decibels (dB).")
        
        with col2:
            parkinsons_dict["Shimmer:APQ3"] = st.number_input("Shimmer:APQ3", format="%.5f", value=None, help="Three-point Amplitude Perturbation Quotient (APQ3): A measure of short-term amplitude variation across three vocal cycles.")
        
        with col3:
            parkinsons_dict["Shimmer:APQ5"] = st.number_input("Shimmer:APQ5", format="%.5f", value=None, help="Five-point Amplitude Perturbation Quotient (APQ5): A measure of short-term amplitude variation across five vocal cycles.")
        
        with col1:
            parkinsons_dict["MDVP:APQ"] = st.number_input("MDVP:APQ", format="%.5f", value=None, help="Eleven-point Amplitude Perturbation Quotient (APQ): A broader measure of amplitude variation across eleven vocal cycles.")
        
        with col2:
            parkinsons_dict["Shimmer:DDA"] = st.number_input("Shimmer:DDA", format="%.5f", value=None, help="Shimmer (DDA): A measure of the average difference between consecutive differences in vocal amplitude.")
        
        with col3:
            parkinsons_dict["NHR"] = st.number_input("NHR", format="%.5f", value=None, help="Noise-to-Harmonics Ratio (NHR): Measures the amount of noise in your voice relative to the clear, harmonic sound. Higher values indicate more hoarseness or breathiness.")
        
        with col1:
            parkinsons_dict["HNR"] = st.number_input("HNR", format="%.5f", value=None, help="Harmonics-to-Noise Ratio (HNR): The inverse of NHR; measures the ratio of clear vocal sound to noise. Higher values indicate a clearer voice.")
        
        with col2:
            parkinsons_dict["RPDE"] = st.number_input("RPDE", format="%.5f", value=None, help="Recurrence Period Density Entropy (RPDE): A measure of the complexity and predictability of the voice signal. Lower values can indicate reduced vocal flexibility.")
        
        with col3:
            parkinsons_dict["DFA"] = st.number_input("DFA", format="%.5f", value=None, help="Detrended Fluctuation Analysis (DFA): Another measure of the fractal scaling properties of the voice signal, related to its long-range correlations.")
        
        with col1:
            parkinsons_dict["spread1"] = st.number_input("Spread1", format="%.5f", value=None, help="Nonlinear Pitch Variation 1 (Spread1): A nonlinear measure of the fundamental frequency variation, capturing subtle irregularities.")
        
        with col2:
            parkinsons_dict["spread2"] = st.number_input("Spread2", format="%.5f", value=None, help="Nonlinear Pitch Variation 2 (Spread2): Another nonlinear measure of pitch variation, providing further insight into voice irregularities.")
        
        with col3:
            parkinsons_dict["D2"] = st.number_input("D2", format="%.5f", value=None, help="Correlation Dimension (D2): A nonlinear measure of the signal's complexity, indicating the fractal dimension of the vocal dynamics.")
        
        with col1:
            parkinsons_dict["PPE"] = st.number_input("PPE", format="%.5f", value=None, help="Pitch Perturbation Entropy (PPE): Measures the chaotic nature or unpredictability of the vocal pitch, where higher values indicate more randomness.")
        parkinsons_check_button = st.form_submit_button(label="Perform Parkinsons Check")
        try:
            if (parkinsons_check_button):
                result = dd.detect_disease(tuple(parkinsons_dict.values()), "parkinsons")
                ai_feedback = generate_feedback(["parkinsons", bool(result)], parkinsons_dict)
                if (result == 1):
                    st.error("Result: Has Parkinsons")
                else:
                    st.success("Result: No Parkinsons")
                st.subheader("Personalized Feedback:")
                st.write("(Note: Generated with AI, use carefully, consult doctor for best advice!)")
                st.write(ai_feedback)
        except ValueError as e:
            st.warning(f"Invalid values! Either empty or too large! Please input all the fields with proper values! {e}")
