"""
Database module for DataGouv Dashboard Builder.
Handles data fetching, SQL query generation, and KPI calculations.
"""

import pandas as pd
import requests
from typing import Dict, List, Optional, Tuple
import json
from datetime import datetime


class DataGouvClient:
    """Client for interacting with data.gouv.fr API."""
    
    BASE_URL = "https://www.data.gouv.fr/api/1"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "DataGouv-Dashboard-Builder/1.0"
        })
    
    def search_datasets(self, query: str, page: int = 1, page_size: int = 10) -> Dict:
        """Search for datasets on data.gouv.fr."""
        url = f"{self.BASE_URL}/datasets/"
        params = {
            "q": query,
            "page": page,
            "page_size": page_size
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_dataset(self, dataset_id: str) -> Dict:
        """Get detailed information about a specific dataset."""
        url = f"{self.BASE_URL}/datasets/{dataset_id}/"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
    
    def get_resource_data(self, resource_url: str, format: str = "csv") -> Optional[pd.DataFrame]:
        """Fetch and parse resource data from URL."""
        try:
            if format.lower() == "csv":
                df = pd.read_csv(resource_url, encoding="utf-8", low_memory=False)
            elif format.lower() in ["json", "geojson"]:
                data = self.session.get(resource_url).json()
                df = pd.json_normalize(data)
            elif format.lower() == "excel" or resource_url.endswith(".xlsx"):
                df = pd.read_excel(resource_url)
            else:
                # Try CSV as default
                df = pd.read_csv(resource_url, encoding="utf-8", low_memory=False)
            return df
        except Exception as e:
            print(f"Error loading resource: {e}")
            return None


class SQLQueryBuilder:
    """Builds SQL queries with full transparency."""
    
    @staticmethod
    def generate_kpi_query(column: str, aggregation: str, table: str = "data") -> str:
        """Generate SQL query for KPI calculation."""
        agg_map = {
            "sum": f"SUM({column})",
            "avg": f"AVG({column})",
            "count": f"COUNT({column})",
            "min": f"MIN({column})",
            "max": f"MAX({column})",
            "distinct": f"COUNT(DISTINCT {column})"
        }
        agg_func = agg_map.get(aggregation, f"SUM({column})")
        return f"SELECT {agg_func} as value FROM {table}"
    
    @staticmethod
    def generate_groupby_query(
        group_column: str, 
        value_column: str, 
        aggregation: str,
        table: str = "data",
        limit: int = 20
    ) -> str:
        """Generate SQL query for grouped data (bar chart)."""
        agg_map = {
            "sum": f"SUM({value_column})",
            "avg": f"AVG({value_column})",
            "count": f"COUNT({value_column})",
            "min": f"MIN({value_column})",
            "max": f"MAX({value_column})"
        }
        agg_func = agg_map.get(aggregation, f"SUM({value_column})")
        return f"""SELECT 
    {group_column} as category,
    {agg_func} as value
FROM {table}
GROUP BY {group_column}
ORDER BY value DESC
LIMIT {limit}"""
    
    @staticmethod
    def generate_time_series_query(
        date_column: str,
        value_column: str,
        aggregation: str,
        table: str = "data",
        date_format: str = "%Y-%m"
    ) -> str:
        """Generate SQL query for time series data."""
        agg_map = {
            "sum": f"SUM({value_column})",
            "avg": f"AVG({value_column})",
            "count": f"COUNT({value_column})",
            "min": f"MIN({value_column})",
            "max": f"MAX({value_column})"
        }
        agg_func = agg_map.get(aggregation, f"SUM({value_column})")
        return f"""SELECT 
    DATE_FORMAT({date_column}, '{date_format}') as period,
    {agg_func} as value
FROM {table}
GROUP BY period
ORDER BY period ASC"""


class DataAnalyzer:
    """Analyzes datasets and generates insights."""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.sql_builder = SQLQueryBuilder()
    
    def detect_column_types(self) -> Dict[str, List[str]]:
        """Auto-detect column types for visualization."""
        numeric_cols = []
        categorical_cols = []
        date_cols = []
        
        for col in self.df.columns:
            if pd.api.types.is_datetime64_any_dtype(self.df[col]):
                date_cols.append(col)
            elif pd.api.types.is_numeric_dtype(self.df[col]):
                numeric_cols.append(col)
            elif self.df[col].dtype == "object":
                # Check if it's a date string
                try:
                    pd.to_datetime(self.df[col].dropna().iloc[:10])
                    date_cols.append(col)
                except:
                    if self.df[col].nunique() < len(self.df) * 0.5:
                        categorical_cols.append(col)
                    else:
                        numeric_cols.append(col)
        
        return {
            "numeric": numeric_cols,
            "categorical": categorical_cols,
            "date": date_cols
        }
    
    def calculate_kpi(self, column: str, aggregation: str) -> Tuple[float, str]:
        """Calculate KPI value and return with SQL query."""
        sql = self.sql_builder.generate_kpi_query(column, aggregation)
        
        if aggregation == "sum":
            value = self.df[column].sum()
        elif aggregation == "avg":
            value = self.df[column].mean()
        elif aggregation == "count":
            value = self.df[column].count()
        elif aggregation == "min":
            value = self.df[column].min()
        elif aggregation == "max":
            value = self.df[column].max()
        elif aggregation == "distinct":
            value = self.df[column].nunique()
        else:
            value = self.df[column].sum()
        
        # Handle NaN/None values
        if pd.isna(value):
            value = 0
        
        return float(value), sql
    
    def get_grouped_data(
        self, 
        group_column: str, 
        value_column: str, 
        aggregation: str,
        limit: int = 20
    ) -> Tuple[pd.DataFrame, str]:
        """Get grouped data for bar chart with SQL query."""
        sql = self.sql_builder.generate_groupby_query(
            group_column, value_column, aggregation, limit=limit
        )
        
        agg_func = {
            "sum": "sum",
            "avg": "mean",
            "count": "count",
            "min": "min",
            "max": "max"
        }.get(aggregation, "sum")
        
        grouped = self.df.groupby(group_column)[value_column].agg(agg_func).reset_index()
        grouped.columns = ["category", "value"]
        grouped = grouped.sort_values("value", ascending=False).head(limit)
        
        return grouped, sql
    
    def get_time_series(
        self,
        date_column: str,
        value_column: str,
        aggregation: str,
        date_format: str = "%Y-%m"
    ) -> Tuple[pd.DataFrame, str]:
        """Get time series data with SQL query."""
        sql = self.sql_builder.generate_time_series_query(
            date_column, value_column, aggregation, date_format=date_format
        )
        
        # Convert to datetime if needed
        if not pd.api.types.is_datetime64_any_dtype(self.df[date_column]):
            df_copy = self.df.copy()
            df_copy[date_column] = pd.to_datetime(df_copy[date_column], errors="coerce")
        else:
            df_copy = self.df.copy()
        
        # Create period column
        df_copy["period"] = df_copy[date_column].dt.strftime(date_format)
        
        agg_func = {
            "sum": "sum",
            "avg": "mean",
            "count": "count",
            "min": "min",
            "max": "max"
        }.get(aggregation, "sum")
        
        ts = df_copy.groupby("period")[value_column].agg(agg_func).reset_index()
        ts.columns = ["period", "value"]
        ts = ts.sort_values("period")
        
        return ts, sql


class DashboardState:
    """Manages dashboard state and configuration."""
    
    @staticmethod
    def initialize_session_state():
        """Initialize Streamlit session state variables."""
        if "dashboard_widgets" not in st.session_state:
            st.session_state.dashboard_widgets = []
        if "current_dataset" not in st.session_state:
            st.session_state.current_dataset = None
        if "current_df" not in st.session_state:
            st.session_state.current_df = None
        if "search_results" not in st.session_state:
            st.session_state.search_results = []


# Import streamlit here to avoid circular imports in session state
import streamlit as st
