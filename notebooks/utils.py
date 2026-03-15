import pandas as pd

def highlight_max_value(row):
    """Highlight the maximum value in a row (excluding 'Metric' column)"""
    styles = [''] * len(row)
    metric_col = 'Metric'
    
    try:
        # Get all numeric values in the row
        values = {}
        for idx, col in enumerate(row.index):
            if col != metric_col:
                try:
                    val = pd.to_numeric(row[col], errors='coerce')
                    if pd.notna(val):
                        values[idx] = val
                except:
                    pass
        
        # Find max value
        if values:
            max_idx = max(values, key=values.get)
            styles[max_idx] = 'background-color: lightgreen; color: black; font-weight: bold'
    except Exception:
        pass
    return styles
