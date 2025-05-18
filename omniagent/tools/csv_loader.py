import pandas as pd
import io

def load_csv(file_content: bytes, delimiter: str = ",") -> pd.DataFrame:
    """
    Loads a CSV file from bytes and returns a DataFrame.

    Args:
        file_content (bytes): Raw bytes from uploaded file (e.g., via Streamlit)
        delimiter (str): Delimiter to use (default ',')

    Returns:
        pd.DataFrame: Parsed table
    """
    try:
        df = pd.read_csv(io.BytesIO(file_content), delimiter=delimiter)
        return df
    except Exception as e:
        raise ValueError(f"❌ Failed to load CSV: {str(e)}")

def dataframe_summary(df: pd.DataFrame) -> str:
    """
    Converts a DataFrame to a human-readable text summary.

    Args:
        df (pd.DataFrame): DataFrame to summarize

    Returns:
        str: Text summary of columns and sample rows
    """
    if df.empty:
        return "📭 CSV is empty or could not be parsed."

    summary = f"📊 CSV Summary:\nColumns: {', '.join(df.columns)}\n"
    summary += f"\nTop 3 rows:\n{df.head(3).to_string(index=False)}"
    return summary
