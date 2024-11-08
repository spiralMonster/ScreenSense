from .get_model import return_model
from .get_input_data import get_data_to_calculate_right_screen_time
from .processing_data import process_data

def get_results():
    data = get_data_to_calculate_right_screen_time()
    data = process_data(data)
    model = return_model()
    pred = model.predict(data)
    pred=pred[0]
    pred=str(pred)+' hours'
    return pred

