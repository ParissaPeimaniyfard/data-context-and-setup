import os
import pandas as pd


class Olist:
    
    def get_data(self):
        
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
        
        abs_path= os.path.abspath(__file__)
        base_dir = os.path.dirname(os.path.dirname(abs_path))
        path_to_folder = os.path.join(base_dir, 'data/csv')
        file_names=[]
        for name in os.listdir(path_to_folder):
            if name.endswith('csv'):
                file_names.append(name)
        #print (file_names)
        key_names=[]
        for file in file_names:
            file= file.replace('_dataset.csv','')
            file= file.replace('.csv','')
            file =file.replace('olist_','')
            key_names.append(file)
        #print (key_names)
        list_DF=[]
        for name in file_names:
            datf= pd.read_csv(os.path.join(path_to_folder, name)).head(1)
            list_DF.append(datf)
        data= dict(zip(key_names, list_DF))
        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
