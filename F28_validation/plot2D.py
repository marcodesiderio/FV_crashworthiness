import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
sns.set()


class plot2D:
    __slots__ = ['x_data', 'y_data', 'label', 'color']