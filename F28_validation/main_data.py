from read_abaqus_data import data


filename = 'AT3_floor'
rootdir = r'C:\Users\marco\OneDrive\Documents\TU Delft\MSc\THESIS\Research Work\data_analysis\FV_crashworthiness\F28_validation\e=0'

ALLKE = data(rootdir, filename, '.csv', filter_data='True')
