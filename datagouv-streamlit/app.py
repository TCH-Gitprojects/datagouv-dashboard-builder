"""
DataGouv Dashboard Builder - Main Application
A modern Streamlit app for visualizing French open data.

Author: Your Name
Version: 1.0.0
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from typing import Dict, List
import json

# Import custom modules
from src.database import DataGouvClient, DataAnalyzer, DashboardState
from src.ui_components import (
    apply_custom_styles, render_header, render_metrics_row,
    render_sql_transparency, create_bar_chart, create_line_chart,
    create_pie_chart, render_dataset_card, render_footer, COLORS
)


# Page Configuration
st.set_page_config(
    page_title="DataGouv Dashboard Builder",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
DashboardState.initialize_session_state()

# Apply custom styles
apply_custom_styles()


def main():
    """Main application entry point."""
    
    # Render header
    render_header()
    
    # Sidebar Navigation
    with st.sidebar:
        st.markdown("### 🧭 Navigation")
        
        page = st.radio(
            "Select Page",
            ["🏠 Home", "🔍 Search Datasets", "📊 Dashboard Builder", "⚙️ Editor Mode"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Current Dataset Info
        if st.session_state.current_dataset:
            st.markdown("### 📁 Current Dataset")
            st.info(f"**{st.session_state.current_dataset.get('title', 'Unknown')[:50]}...**")
            
            if st.session_state.current_df is not None:
                st.caption(f"📊 {len(st.session_state.current_df):,} rows × {len(st.session_state.current_df.columns)} columns")
        
        st.markdown("---")
        st.markdown("### 📚 Resources")
        st.markdown("- [data.gouv.fr](https://www.data.gouv.fr)")
        st.markdown("- [API Documentation](https://www.data.gouv.fr/fr/apidoc/)")
    
    # Route to appropriate page
    if page == "🏠 Home":
        render_home_page()
    elif page == "🔍 Search Datasets":
        render_search_page()
    elif page == "📊 Dashboard Builder":
        render_dashboard_page()
    elif page == "⚙️ Editor Mode":
        render_editor_page()
    
    # Render footer
    render_footer()


def render_home_page():
    """Render the home/landing page."""
    
    # Hero Section
    st.markdown("""
    <div style="text-align: center; padding: 3rem 1rem;">
        <div style="display: inline-block; background: linear-gradient(135deg, #4F46E5 0%, #3730A3 100%); 
                    color: white; padding: 0.5rem 1rem; border-radius: 9999px; font-size: 0.875rem; font-weight: 500; margin-bottom: 1.5rem;">
            🚀 No-code dashboard builder for French open data
        </div>
        <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 1rem; line-height: 1.2;">
            Turn data.gouv.fr datasets<br>
            <span style="color: #4F46E5;">into insights instantly</span>
        </h1>
        <p style="font-size: 1.25rem; color: #64748B; max-width: 600px; margin: 0 auto 2rem;">
            Search, analyze, and visualize open data from the French government.
            Automatic dashboard generation with transparent SQL queries.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔍 Browse Datasets", use_container_width=True):
            st.session_state.page = "🔍 Search Datasets"
            st.rerun()
    
    # Features Section
    st.markdown("---")
    st.markdown("## ✨ Key Features")
    
    features = [
        {
            "icon": "🔍",
            "title": "Search & Connect",
            "description": "Browse thousands of datasets from data.gouv.fr. Find data on economy, environment, transport, and more."
        },
        {
            "icon": "📊",
            "title": "Auto-Generate Dashboards",
            "description": "Our AI analyzes your data and creates relevant visualizations automatically. Bar charts, line graphs, pie charts, and stats."
        },
        {
            "icon": "🔎",
            "title": "Transparent SQL",
            "description": "See exactly what queries are run to generate each visualization. Full transparency into how your data is processed."
        }
    ]
    
    cols = st.columns(3)
    for i, feature in enumerate(features):
        with cols[i]:
            st.markdown(f"""
            <div style="background: white; border: 1px solid #E2E8F0; border-radius: 16px; padding: 1.5rem; height: 100%;">
                <div style="font-size: 2.5rem; margin-bottom: 1rem;">{feature['icon']}</div>
                <h3 style="font-weight: 600; margin-bottom: 0.75rem;">{feature['title']}</h3>
                <p style="color: #64748B; font-size: 0.95rem; line-height: 1.6;">{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # How It Works Section
    st.markdown("---")
    st.markdown("## 🔄 How It Works")
    
    steps = [
        ("1", "Search", "Find datasets on data.gouv.fr"),
        ("2", "Select", "Choose a data resource"),
        ("3", "Analyze", "We auto-detect data types"),
        ("4", "Visualize", "Dashboard generates instantly")
    ]
    
    step_cols = st.columns(4)
    for i, (num, title, desc) in enumerate(steps):
        with step_cols[i]:
            st.markdown(f"""
            <div style="text-align: center;">
                <div style="
                    width: 60px;
                    height: 60px;
                    background: linear-gradient(135deg, #4F46E5 0%, #3730A3 100%);
                    color: white;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 1.5rem;
                    font-weight: 700;
                    margin: 0 auto 1rem;
                ">{num}</div>
                <h4 style="font-weight: 600; margin-bottom: 0.5rem;">{title}</h4>
                <p style="color: #64748B; font-size: 0.875rem;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)


def render_search_page():
    """Render the dataset search page."""
    
    st.markdown("## 🔍 Search Datasets")
    st.markdown("Find datasets from data.gouv.fr to analyze and visualize.")
    
    # Search input
    search_col1, search_col2 = st.columns([4, 1])
    with search_col1:
        search_query = st.text_input(
            "Search",
            placeholder="Search for datasets (e.g., 'economy', 'environment', 'transport')...",
            label_visibility="collapsed"
        )
    with search_col2:
        search_button = st.button("🔍 Search", use_container_width=True)
    
    # Perform search
    if search_button and search_query:
        with st.spinner("Searching data.gouv.fr..."):
            client = DataGouvClient()
            try:
                results = client.search_datasets(search_query, page_size=10)
                st.session_state.search_results = results.get("data", [])
            except Exception as e:
                st.error(f"Error searching datasets: {e}")
    
    # Display results
    if st.session_state.search_results:
        st.markdown(f"### 📊 Found {len(st.session_state.search_results)} datasets")
        
        for i, dataset in enumerate(st.session_state.search_results):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                title = dataset.get("title", "Untitled Dataset")
                description = dataset.get("description", "No description available.")
                organization = dataset.get("organization", {}).get("name", "Unknown Organization")
                resources_count = len(dataset.get("resources", []))
                
                if len(description) > 200:
                    description = description[:200] + "..."
                
                st.markdown(f"""
                <div style="background: white; border: 1px solid #E2E8F0; border-radius: 12px; padding: 1.25rem; margin-bottom: 0.5rem;">
                    <h4 style="margin: 0 0 0.5rem 0; font-weight: 600;">{title}</h4>
                    <p style="margin: 0 0 0.75rem 0; color: #64748B; font-size: 0.875rem; line-height: 1.5;">{description}</p>
                    <div style="display: flex; gap: 0.75rem; align-items: center;">
                        <span style="background: #4F46E520; color: #4F46E5; padding: 0.25rem 0.75rem; border-radius: 9999px; font-size: 0.75rem; font-weight: 600;">
                            📁 {resources_count} resources
                        </span>
                        <span style="color: #64748B; font-size: 0.75rem;">{organization}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.write("")
                st.write("")
                if st.button("Select", key=f"select_{i}", use_container_width=True):
                    st.session_state.current_dataset = dataset
                    
                    # Try to load the first CSV resource
                    resources = dataset.get("resources", [])
                    csv_resources = [r for r in resources if r.get("format", "").lower() in ["csv", ""]]
                    
                    if csv_resources:
                        with st.spinner("Loading dataset..."):
                            client = DataGouvClient()
                            resource_url = csv_resources[0].get("url")
                            df = client.get_resource_data(resource_url, "csv")
                            
                            if df is not None:
                                st.session_state.current_df = df
                                st.success(f"✅ Loaded {len(df):,} rows!")
                                st.rerun()
                            else:
                                st.error("Failed to load dataset")
                    else:
                        st.warning("No CSV resources found")


def render_dashboard_page():
    """Render the dashboard builder page."""
    
    st.markdown("## 📊 Dashboard Builder")
    
    if st.session_state.current_df is None:
        st.info("👈 Please select a dataset from the Search page first.")
        return
    
    df = st.session_state.current_df
    analyzer = DataAnalyzer(df)
    column_types = analyzer.detect_column_types()
    
    # Dataset Overview
    with st.expander("📁 Dataset Overview", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Rows", f"{len(df):,}")
        with col2:
            st.metric("Total Columns", len(df.columns))
        with col3:
            st.metric("Missing Values", f"{df.isnull().sum().sum():,}")
        
        st.markdown("**Column Types Detected:**")
        type_cols = st.columns(3)
        with type_cols[0]:
            st.markdown(f"📊 Numeric: {len(column_types['numeric'])}")
        with type_cols[1]:
            st.markdown(f"🏷️ Categorical: {len(column_types['categorical'])}")
        with type_cols[2]:
            st.markdown(f"📅 Date: {len(column_types['date'])}")
    
    # KPI Configuration
    st.markdown("---")
    st.markdown("### 📈 Key Performance Indicators")
    
    if column_types["numeric"]:
        kpi_cols = st.columns(3)
        
        for i in range(3):
            with kpi_cols[i]:
                with st.container(border=True):
                    st.markdown(f"**KPI {i+1}**")
                    
                    kpi_col = st.selectbox(
                        f"Column {i+1}",
                        column_types["numeric"],
                        key=f"kpi_col_{i}"
                    )
                    
                    kpi_agg = st.selectbox(
                        f"Aggregation {i+1}",
                        ["sum", "avg", "count", "min", "max", "distinct"],
                        key=f"kpi_agg_{i}"
                    )
                    
                    if kpi_col:
                        value, sql = analyzer.calculate_kpi(kpi_col, kpi_agg)
                        
                        # Format display
                        if value > 1000000:
                            display_value = f"{value/1000000:.2f}M"
                        elif value > 1000:
                            display_value = f"{value/1000:.1f}K"
                        else:
                            display_value = f"{value:,.0f}"
                        
                        st.markdown(f"""
                        <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #F8FAFC 0%, white 100%); border-radius: 12px; margin-top: 0.5rem;">
                            <div style="font-size: 2rem; font-weight: 700; color: #4F46E5;">{display_value}</div>
                            <div style="font-size: 0.75rem; color: #64748B; text-transform: uppercase;">{kpi_agg} of {kpi_col}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        render_sql_transparency(sql, "🔍 View SQL")
    
    # Visualization Builder
    st.markdown("---")
    st.markdown("### 📊 Visualizations")
    
    viz_tab1, viz_tab2, viz_tab3 = st.tabs(["📊 Bar Chart", "📈 Line Chart", "🥧 Pie Chart"])
    
    # Bar Chart
    with viz_tab1:
        if column_types["categorical"] and column_types["numeric"]:
            bar_cols = st.columns(3)
            
            with bar_cols[0]:
                bar_x = st.selectbox("Category Column", column_types["categorical"], key="bar_x")
            with bar_cols[1]:
                bar_y = st.selectbox("Value Column", column_types["numeric"], key="bar_y")
            with bar_cols[2]:
                bar_agg = st.selectbox("Aggregation", ["sum", "avg", "count", "min", "max"], key="bar_agg")
            
            if bar_x and bar_y:
                grouped_df, sql = analyzer.get_grouped_data(bar_x, bar_y, bar_agg, limit=15)
                
                fig = create_bar_chart(
                    grouped_df,
                    "category",
                    "value",
                    title=f"{bar_agg.title()} of {bar_y} by {bar_x}",
                    orientation="h"
                )
                
                st.plotly_chart(fig, use_container_width=True)
                render_sql_transparency(sql, "🔍 View SQL Query")
        else:
            st.warning("Need at least one categorical and one numeric column for bar charts.")
    
    # Line Chart
    with viz_tab2:
        if column_types["date"] and column_types["numeric"]:
            line_cols = st.columns(3)
            
            with line_cols[0]:
                line_x = st.selectbox("Date Column", column_types["date"], key="line_x")
            with line_cols[1]:
                line_y = st.selectbox("Value Column", column_types["numeric"], key="line_y")
            with line_cols[2]:
                line_agg = st.selectbox("Aggregation", ["sum", "avg", "count", "min", "max"], key="line_agg")
            
            if line_x and line_y:
                ts_df, sql = analyzer.get_time_series(line_x, line_y, line_agg)
                
                fig = create_line_chart(
                    ts_df,
                    "period",
                    "value",
                    title=f"{line_agg.title()} of {line_y} over time"
                )
                
                st.plotly_chart(fig, use_container_width=True)
                render_sql_transparency(sql, "🔍 View SQL Query")
        else:
            st.warning("Need at least one date and one numeric column for line charts.")
    
    # Pie Chart
    with viz_tab3:
        if column_types["categorical"] and column_types["numeric"]:
            pie_cols = st.columns(3)
            
            with pie_cols[0]:
                pie_names = st.selectbox("Category Column", column_types["categorical"], key="pie_names")
            with pie_cols[1]:
                pie_values = st.selectbox("Value Column", column_types["numeric"], key="pie_values")
            with pie_cols[2]:
                pie_agg = st.selectbox("Aggregation", ["sum", "avg", "count"], key="pie_agg")
            
            if pie_names and pie_values:
                pie_df, sql = analyzer.get_grouped_data(pie_names, pie_values, pie_agg, limit=8)
                
                fig = create_pie_chart(
                    pie_df,
                    "category",
                    "value",
                    title=f"Distribution of {pie_values} by {pie_names}"
                )
                
                st.plotly_chart(fig, use_container_width=True)
                render_sql_transparency(sql, "🔍 View SQL Query")
        else:
            st.warning("Need at least one categorical and one numeric column for pie charts.")
    
    # Data Preview
    st.markdown("---")
    st.markdown("### 👁️ Data Preview")
    
    with st.expander("View Raw Data"):
        st.dataframe(df.head(100), use_container_width=True)


def render_editor_page():
    """Render the drag-and-drop editor mode."""
    
    st.markdown("## ⚙️ Dashboard Editor")
    st.markdown("Create custom layouts with our grid-based editor.")
    
    if st.session_state.current_df is None:
        st.info("👈 Please select a dataset first to use the editor.")
        return
    
    # Grid Layout System
    st.markdown("### 📐 Grid Layout")
    
    # Layout configuration
    layout_col1, layout_col2 = st.columns([1, 3])
    
    with layout_col1:
        st.markdown("**Layout Settings**")
        
        num_rows = st.number_input("Number of Rows", min_value=1, max_value=5, value=2)
        cols_per_row = st.selectbox("Columns per Row", [1, 2, 3, 4], index=1)
        
        st.markdown("---")
        st.markdown("**Add Widget**")
        
        widget_type = st.selectbox(
            "Widget Type",
            ["📊 Bar Chart", "📈 Line Chart", "🥧 Pie Chart", "🔢 Metric", "📋 Data Table"]
        )
        
        if st.button("➕ Add to Grid", use_container_width=True):
            new_widget = {
                "id": f"widget_{len(st.session_state.dashboard_widgets)}",
                "type": widget_type,
                "position": len(st.session_state.dashboard_widgets)
            }
            st.session_state.dashboard_widgets.append(new_widget)
            st.success(f"Added {widget_type}!")
            st.rerun()
    
    with layout_col2:
        st.markdown("**Dashboard Preview**")
        
        if not st.session_state.dashboard_widgets:
            st.info("Add widgets from the sidebar to build your dashboard.")
        else:
            # Render grid
            widgets = st.session_state.dashboard_widgets
            
            for row_idx in range(num_rows):
                row_widgets = widgets[row_idx * cols_per_row:(row_idx + 1) * cols_per_row]
                
                if row_widgets:
                    cols = st.columns(cols_per_row)
                    
                    for col_idx, widget in enumerate(row_widgets):
                        with cols[col_idx]:
                            with st.container(border=True):
                                st.markdown(f"**{widget['type']}**")
                                
                                # Widget configuration
                                df = st.session_state.current_df
                                analyzer = DataAnalyzer(df)
                                column_types = analyzer.detect_column_types()
                                
                                if widget['type'] == "🔢 Metric" and column_types["numeric"]:
                                    metric_col = st.selectbox(
                                        "Column",
                                        column_types["numeric"],
                                        key=f"edit_metric_col_{widget['id']}"
                                    )
                                    metric_agg = st.selectbox(
                                        "Aggregation",
                                        ["sum", "avg", "count", "min", "max"],
                                        key=f"edit_metric_agg_{widget['id']}"
                                    )
                                    
                                    if metric_col:
                                        value, sql = analyzer.calculate_kpi(metric_col, metric_agg)
                                        st.metric(
                                            label=f"{metric_agg.title()} of {metric_col}",
                                            value=f"{value:,.0f}"
                                        )
                                
                                elif widget['type'] == "📊 Bar Chart" and column_types["categorical"] and column_types["numeric"]:
                                    bar_x = st.selectbox(
                                        "Category",
                                        column_types["categorical"],
                                        key=f"edit_bar_x_{widget['id']}"
                                    )
                                    bar_y = st.selectbox(
                                        "Value",
                                        column_types["numeric"],
                                        key=f"edit_bar_y_{widget['id']}"
                                    )
                                    
                                    if bar_x and bar_y:
                                        grouped_df, _ = analyzer.get_grouped_data(bar_x, bar_y, "sum", limit=10)
                                        fig = create_bar_chart(grouped_df, "category", "value", height=250)
                                        st.plotly_chart(fig, use_container_width=True, key=f"chart_{widget['id']}")
                                
                                elif widget['type'] == "📋 Data Table":
                                    st.dataframe(df.head(5), use_container_width=True)
                                
                                else:
                                    st.caption("Configure this widget...")
                                
                                # Remove button
                                if st.button("🗑️ Remove", key=f"remove_{widget['id']}"):
                                    st.session_state.dashboard_widgets.remove(widget)
                                    st.rerun()
    
    # Clear all button
    if st.session_state.dashboard_widgets:
        if st.button("🗑️ Clear All Widgets", type="secondary"):
            st.session_state.dashboard_widgets = []
            st.rerun()


if __name__ == "__main__":
    main()
