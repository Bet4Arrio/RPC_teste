import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots




def abc_pie(df: go.Figure, class_column:str, max_column:str) -> go.Figure:
    values2 = df.groupby(class_column).sum().reset_index()

    return px.pie(values2, values=max_column, names=class_column, title='Representação porcentural dos grupos')

def abc_curve(df: go.Figure, class_column:str, 
                accumulative_columns:list, max_column:str) -> go.Figure:

    values = df.groupby(class_column).sum().reset_index()
    values2 = df.groupby(class_column).max().reset_index()
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
    go.Bar(x=values[class_column], y=values[accumulative_columns[0]], 
        marker=dict(color = list(map(lambda x: "#fd084a", values[class_column]))), name="Renda Anual"),
    secondary_y=False
    )
    fig.add_trace(
        go.Bar(x=values[class_column], y=values[accumulative_columns[1]], 
            marker=dict(color = list(map(lambda x: "#494fc1", values[class_column]))), name="Dividas"),
        secondary_y=False,

        )
    fig.add_trace(
    go.Scatter(x=values2[class_column], y=values2[max_column], name="Porcentagem de renda anual"),
    secondary_y=True
    )

    return fig