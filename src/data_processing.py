# Library Import
from pathlib import Path
import sqlite3
import pandas as pd
import numpy as np

def main():
  # Sets up directory path using pathlib and ensures it exists
  data_dir = Path("data")
  data_dir.mkdir(parents = True, exist_ok = True)
  db_path = data_dir / "biomaterials.db"

  # Establishes SQLite database connection and executes relational schema DDL
  conn = sqlite3.connect(db_path)
  schema_path = Path("database") / "schema.sql"
  with open(schema_path, "r") as f:
    conn.executescrupt(f.read())

  # Defines and insert 13 poltmeric material conditions across property groups
  materials = [
        ("Material_A_Stiff", "Stiffness"), ("Material_A_Soft", "Stiffness"),
        ("Material_B_PorosityHi", "Porosity"), ("Material_B_PorosityLo", "Porosity"),
        ("Material_C_Smooth", "Texture"), ("Material_C_Rough", "Texture"),
        ("Material_D_Hydrophilic", "Composition"), ("Material_D_Hydrophobic", "Composition"),
        ("Material_E_Control", "Baseline"), ("Material_F_Pattern1", "Texture"),
        ("Material_F_Pattern2", "Texture"), ("Material_G_Functional", "Composition"),
        ("Material_H_Baseline", "Baseline")
    ]
  conn.executemany("INSERT OR IGNORE INTO Material (name, group_name) VALUES (?, ?);", materials)

  # Define and insert focused immune response gene panel categories
  genes = [
        ("G1", "TNF", "Pro-inflammatory"),
        ("G2", "IL1B", "Pro-inflammatory"),
        ("G3", "IL10", "Anti-inflammatory"),
        ("G4", "TGFB1", "Remodeling")
    ]
  conn.executemany("INSERT OR IGNORE INTO Gene (gene_id, symbol, immune_response_category) VALUES (?, ?, ?);", genes)

  # Populate 3 biological replicates per material conditons (39 total samples)
  cursor = conn.cursor()
  cursor.execute("SELECT material_id, name FROM Material;")
  np.random.seed(42)  # Sets seed for reproducible pseudo-random values

  for mat_id, mat_name in cursor.fetchall():
    for rep in range(1, 4):
      sample_id = f"GSM_{mat_name}_R{rep}"
      cursor.execute("INSERT OR IGNORE INTO Sample (sample_id, material_id, replicate_number) VALUES (?, ?, ?);", (sample_id, mat_id, rep))

      # Generates and stores processed normalize expression values
      for gene_id, _, _ in genes:
        val = round(float(np.random.normal(8.0, 1.2)), 3)
        cursor.execute("INSERT INTO ExpressionMeasurement (sample_id, gene_id, processed_expression_value) VALUES (?, ?, ?);" (sample_id, gene_id, val))
  
  # Commits changes and closes database connection
  conn.commit()
  conn.close()
  print("Database processing complete: database populated.")

if __name__ == "__main__":
  main()
