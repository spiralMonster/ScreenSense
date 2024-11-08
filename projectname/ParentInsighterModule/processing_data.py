import json
import numpy as np
def process_data(data):
    with open('projectname/ParentInsighterModule/class_indices.json','r') as file:
        class_indices=json.load(file)

    categorical_feat=['StudyHabits','HeadacheHistory','HistoryOfEyeProblems','EmotionalHealth']
    for feat in categorical_feat:
        data[feat]=class_indices[data[feat]]

    results=list(data.values())
    results=[float(a) for a in results]
    results=np.array(results)
    results=np.expand_dims(results,axis=0)

    return results



