import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np
def treemap(df:go.Figure, group_column, value_column) -> go.Figure:
    fig = px.treemap(df, path=[group_column, "house"], values=value_column,
                    color=value_column, hover_data=[value_column],
                    color_continuous_scale='RdBu',
                    color_continuous_midpoint=np.average(df[value_column]))
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    return fig