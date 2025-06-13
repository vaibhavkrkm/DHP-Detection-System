import google.generativeai as genai

api_key = "AIzaSyCFn0Wz5-5kK75njb59vFcA8YfDhWdn39s"
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_feedback(disease_info, parameters):
    parameters_str = str(parameters)
    try:
        if (disease_info[1] == True):
            return model.generate_content(f"Generate simple feedback(having at most 5 points) for a person who has {disease_info[0]} with following parameters: {parameters_str}, also create 2 sections namely '✅ What to do' and '❌ What to avoid' in this situation").text
        else:
            return model.generate_content(f"Generate simple feedback (having at most 5 points) for a person who currently does not have {disease_info[0]} but he/she has following parameters: {parameters_str}").text
    except Exception as e:
        return f"An error occured: {e}"


if (__name__ == "__main__"):
    sample_parameters = {
        "pregnancies": 1,
        "glucose": 89,
        "blood_pressure": 66,
        "skin_thickness": 23,
        "insulin": 94,
        "bmi": 28.1,
        "diabetes_pedigree_function": 0.167,
        "age": 21,
        }
    sample_disease_info = ("diabetes", False)
    
    print(generate_feedback(sample_disease_info, sample_parameters))
