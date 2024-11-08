import joblib
from sklearn.ensemble import RandomForestRegressor

def return_model():
    with open("projectname/ParentInsighterModule/screen_time_predictor.joblib", "rb") as file:
        model = joblib.load(file)

    return model