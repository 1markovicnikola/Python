import matplotlib.pyplot as plt
import datetime as _dt
import pandas as pd

class Csv():
    def __init__(self, file_path):
        self.csv_file = pd.read_csv(self.file_path)

    def update_needed(self):
        if list(self.csv_file['data'])[-1] == _dt.datetime.today().date().strftime('%Y/%m/%d'):
            return False
        return True
    
    def update(self):
        


