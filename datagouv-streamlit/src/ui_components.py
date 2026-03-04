"""
UI Components module for DataGouv Dashboard Builder.
Reusable components for modern SaaS design.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, List, Optional, Tuple


# Color Palette - Modern Slate/Indigo SaaS Theme
COLORS = {
    "primary": "#4F46E5",      # Indigo 600
    "primary_light": "#818CF8", # Indigo 400
    "primary_dark": "#3730A3",  # Indigo 800
    "secondary": "#64748B",     # Slate 500
    "background": "#F8FAFC",    # Slate 50
    "surface": "#FFFFFF",       # White
    "text": "#1E293B",          # Slate 800
    "text_muted": "#64748B",    # Slate 500
    "border": "#E2E8F0",        # Slate 200
    "success": "#10B981",       # Emerald 500
    "warning": "#F59E0B",       # Amber 500
    "error": "#EF4444",         # Red 500
    "chart_colors": ["#4F46E5", "#06B6D4", "#8B5CF6", "#EC4899", "#10B981", "#F59E0B"]
}


def apply_custom_styles():
    """Apply custom CSS styles for modern SaaS look."""
    st.markdown(f"""
    <style>
    /* Main container styling */
    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }}
    
    /* Typography */
    h1 {{
        color: {COLORS["text"]};
        font-weight: 700;
        letter-spacing: -0.025em;
    }}
    
    h2, h3 {{
        color: {COLORS["text"]};
        font-weight: 600;
        letter-spacing: -0.025em;
    }}
    
    /* Metric cards */
    .metric-card {{
        background: linear-gradient(135deg, {COLORS["surface"]} 0%, {COLORS["background"]} 100%);
        border: 1px solid {COLORS["border"]};
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: all 0.2s ease;
    }}
    
    .metric-card:hover {{
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }}
    
    .metric-value {{
        font-size: 2.5rem;
        font-weight: 700;
        color: {COLORS["primary"]};
        line-height: 1.2;
    }}
    
    .metric-label {{
        font-size: 0.875rem;
        color: {COLORS["text_muted"]};
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}
    
    /* SQL query display */
    .sql-container {{
        background: #1E293B;
        border-radius: 12px;
        padding: 1rem;
        margin-top: 0.5rem;
    }}
    
    .sql-code {{
        color: #E2E8F0;
        font-family: 'Monaco', 'Menlo', monospace;
        font-size: 0.875rem;
        line-height: 1.5;
        white-space: pre-wrap;
    }}
    
    /* Section containers */
    .section-container {{
        background: {COLORS["surface"]};
        border: 1px solid {COLORS["border"]};
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }}
    
    /* Button styling override */
    .stButton > button {{
        background: linear-gradient(135deg, {COLORS["primary"]} 0%, {COLORS["primary_dark"]} 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.2s ease;
    }}
    
    .stButton > button:hover {{
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.4);
        transform: translateY(-1px);
    }}
    
    /* Input styling */
    .stTextInput > div > div > input {{
        border-radius: 10px;
        border: 1px solid {COLORS["border"]};
        padding: 0.75rem 1rem;
    }}
    
    /* Select box styling */
    .stSelectbox > div > div > div {{
        border-radius: 10px;
        border: 1px solid {COLORS["border"]};
    }}
    
    /* Dataframe styling */
    .dataframe {{
        border-radius: 12px;
        overflow: hidden;
    }}
    
    /* Sidebar styling */
    .css-1d391kg {{
        background: {COLORS["background"]};
    }}
    
    /* Expander styling */
    .streamlit-expanderHeader {{
        background: {COLORS["background"]};
        border-radius: 10px;
        font-weight: 600;
    }}
    
    /* Chart container */
    .chart-container {{
        background: {COLORS["surface"]};
        border: 1px solid {COLORS["border"]};
        border-radius: 16px;
        padding: 1rem;
    }}
    
    /* Badge styling */
    .badge {{
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }}
    
    .badge-primary {{
        background: {COLORS["primary"]}20;
        color: {COLORS["primary"]};
    }}
    
    .badge-success {{
        background: {COLORS["success"]}20;
        color: {COLORS["success"]};
    }}
    
    /* Hide default Streamlit elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)


def render_header():
    """Render the app header with logo and navigation."""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 0.75rem;">
            <div style="
                width: 40px;
                height: 40px;
                background: linear-gradient(135deg, {COLORS["primary"]} 0%, {COLORS["primary_dark"]} 100%);
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
            ">
                <span style="color: white; font-size: 1.25rem;">📊</span>
            </div>
            <div>
                <span style="font-weight: 700; font-size: 1.25rem; color: {COLORS["text"]};">
                    DataGouv
                </span>
                <span style="font-weight: 500; font-size: 1rem; color: {COLORS["text_muted"]};">
                    Builder
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="text-align: right;">
            <a href="https://www.data.gouv.fr" target="_blank" style="
                color: {COLORS["text_muted"]};
                text-decoration: none;
                font-size: 0.875rem;
                font-weight: 500;
            ">
                data.gouv.fr →
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")


def render_metric_card(
    value: float,
    label: str,
    delta: Optional[float] = None,
    prefix: str = "",
    suffix: str = "",
    decimals: int = 0
) -> str:
    """Render a metric card with optional delta indicator."""
    formatted_value = f"{prefix}{value:,.{decimals}f}{suffix}"
    
    delta_html = ""
    if delta is not None:
        delta_color = COLORS["success"] if delta >= 0 else COLORS["error"]
        delta_icon = "↑" if delta >= 0 else "↓"
        delta_html = f"""
        <span style="color: {delta_color}; font-size: 0.875rem; font-weight: 600; margin-left: 0.5rem;">
            {delta_icon} {abs(delta):.1f}%
        </span>
        """
    
    return f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div style="display: flex; align-items: baseline; margin-top: 0.5rem;">
            <span class="metric-value">{formatted_value}</span>
            {delta_html}
        </div>
    </div>
    """


def render_metrics_row(metrics: List[Dict]):
    """Render a row of metric cards."""
    cols = st.columns(len(metrics))
    
    for i, metric in enumerate(metrics):
        with cols[i]:
            st.markdown(render_metric_card(
                value=metric.get("value", 0),
                label=metric.get("label", ""),
                delta=metric.get("delta"),
                prefix=metric.get("prefix", ""),
                suffix=metric.get("suffix", ""),
                decimals=metric.get("decimals", 0)
            ), unsafe_allow_html=True)


def render_sql_transparency(sql_query: str, title: str = "🔍 SQL Query"):
    """Render SQL query with transparency toggle."""
    with st.expander(title):
        st.markdown(f"""
        <div class="sql-container">
            <div class="sql-code">{sql_query}</div>
        </div>
        """, unsafe_allow_html=True)


def create_bar_chart(
    df: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str = "",
    orientation: str = "v",
    height: int = 400
) -> go.Figure:
    """Create a styled bar chart."""
    if orientation == "h":
        fig = px.bar(
            df,
            y=x_column,
            x=y_column,
            orientation="h",
            title=title,
            color_discrete_sequence=COLORS["chart_colors"]
        )
    else:
        fig = px.bar(
            df,
            x=x_column,
            y=y_column,
            title=title,
            color_discrete_sequence=COLORS["chart_colors"]
        )
    
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color=COLORS["text"]),
        title_font_size=16,
        title_font_weight=600,
        showlegend=False,
        margin=dict(l=40, r=40, t=60, b=40),
        height=height,
        xaxis=dict(
            showgrid=True,
            gridcolor=COLORS["border"],
            gridwidth=1,
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor=COLORS["border"],
            gridwidth=1,
        )
    )
    
    fig.update_traces(
        marker_color=COLORS["primary"],
        marker_line_color=COLORS["primary_dark"],
        marker_line_width=1,
        opacity=0.9,
        hovertemplate="<b>%{x}</b><br>Value: %{y:,.0f}<extra></extra>"
    )
    
    return fig


def create_line_chart(
    df: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str = "",
    height: int = 400
) -> go.Figure:
    """Create a styled line chart for time series."""
    fig = px.line(
        df,
        x=x_column,
        y=y_column,
        title=title,
        color_discrete_sequence=COLORS["chart_colors"]
    )
    
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color=COLORS["text"]),
        title_font_size=16,
        title_font_weight=600,
        showlegend=False,
        margin=dict(l=40, r=40, t=60, b=40),
        height=height,
        xaxis=dict(
            showgrid=True,
            gridcolor=COLORS["border"],
            gridwidth=1,
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor=COLORS["border"],
            gridwidth=1,
        )
    )
    
    fig.update_traces(
        line_color=COLORS["primary"],
        line_width=3,
        marker_color=COLORS["surface"],
        marker_line_color=COLORS["primary"],
        marker_line_width=2,
        marker_size=8,
        fill="tozeroy",
        fillcolor=f"{COLORS['primary']}20",
        hovertemplate="<b>%{x}</b><br>Value: %{y:,.0f}<extra></extra>"
    )
    
    return fig


def create_pie_chart(
    df: pd.DataFrame,
    names_column: str,
    values_column: str,
    title: str = "",
    height: int = 400
) -> go.Figure:
    """Create a styled pie/donut chart."""
    fig = px.pie(
        df,
        names=names_column,
        values=values_column,
        title=title,
        color_discrete_sequence=COLORS["chart_colors"],
        hole=0.5
    )
    
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color=COLORS["text"]),
        title_font_size=16,
        title_font_weight=600,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=40, r=40, t=60, b=80),
        height=height
    )
    
    fig.update_traces(
        textinfo="percent+label",
        textposition="outside",
        hovertemplate="<b>%{label}</b><br>Value: %{value:,.0f}<br>Percentage: %{percent}<extra></extra>"
    )
    
    return fig


def render_dataset_card(dataset: Dict, index: int):
    """Render a dataset search result card."""
    title = dataset.get("title", "Untitled Dataset")
    description = dataset.get("description", "No description available.")
    organization = dataset.get("organization", {}).get("name", "Unknown Organization")
    resources_count = len(dataset.get("resources", []))
    
    # Truncate description
    if len(description) > 200:
        description = description[:200] + "..."
    
    st.markdown(f"""
    <div style="
        background: {COLORS["surface"]};
        border: 1px solid {COLORS["border"]};
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1rem;
        transition: all 0.2s ease;
    " class="dataset-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
                <h4 style="margin: 0 0 0.5rem 0; color: {COLORS["text"]}; font-weight: 600;">
                    {title}
                </h4>
                <p style="margin: 0 0 0.75rem 0; color: {COLORS["text_muted"]}; font-size: 0.875rem; line-height: 1.5;">
                    {description}
                </p>
                <div style="display: flex; gap: 0.75rem; align-items: center;">
                    <span class="badge badge-primary">📁 {resources_count} resources</span>
                    <span style="color: {COLORS["text_muted"]}; font-size: 0.75rem;">
                        {organization}
                    </span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    return st.button(f"Select Dataset", key=f"select_dataset_{index}", use_container_width=True)


def render_widget_editor(widget_id: str, widget_config: Dict):
    """Render widget configuration editor."""
    st.markdown(f"""
    <div style="
        background: {COLORS["background"]};
        border: 2px dashed {COLORS["border"]};
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        color: {COLORS["text_muted"]};
    ">
        <p>Widget Editor Placeholder</p>
        <p style="font-size: 0.875rem;">Configure your visualization here</p>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    """Render the app footer."""
    st.markdown("---")
    st.markdown(f"""
    <div style="
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0;
        color: {COLORS["text_muted"]};
        font-size: 0.875rem;
    ">
        <div>
            Powered by <a href="https://www.data.gouv.fr" target="_blank" style="color: {COLORS["primary"]}; text-decoration: none; font-weight: 500;">data.gouv.fr</a>
        </div>
        <div>
            Built with Python, Streamlit & Plotly
        </div>
    </div>
    """, unsafe_allow_html=True)
