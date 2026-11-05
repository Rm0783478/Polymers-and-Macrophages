from pathlib import Path
import sqlite3
import pandas as pd 
import numpy as np 

def main ():
    # Locates SQLite database file
    db_path = Path("data") / "biomaterials.db"
    if not db_path.exists():
        print("Database not found. Please run data_processing.py first")
        return
    
    # Queries relational database using sqlite3 and pandas
    conn = sqlite3.connect(db_path)
    query = """
        SELECT m.group_name, g.symbol, e.processed_expression_value
        FROM ExpressionMeasurement e
        JOIN Sample s ON e.sample_id = s.sample_id
        JOIN Material m ON s.material_id = m.material_id
        JOIN Gene g ON e.gene_id = g.gene_id;
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Performs statsitical calculations using pandas and numpy aggregations
    summary = df.groupby(['group_name', 'symbol'])['processed_expression_value'].agg(
        Mean = np.mean,
        Std = np.std,
        Median = np.median,
        Count = 'count'
    ).round(3)

    print("--- Summary Statistics ---")
    print(summary)

    # Save aggregated summary statsitics to output directory
    output_dir = Path("output")
    output_dir.mkdir(parents = True, exist_ok = True)
    out_path = output_dir / "summary_statistics.csv"
    summary.to_csv(out_path)
    print(f"Summary saved to {out_path}")

if __name__ == "__main__":
    main()