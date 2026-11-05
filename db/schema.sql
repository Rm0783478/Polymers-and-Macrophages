-- Relational Database Schema for GSE301422 Macrophage Biomaterial Analysis
-- Author: Rohan Mishra

PRAGMA foreign_keys = ON;

-- Material Table: Stores each tested polymeric material condition and its property group
CREATE TABLE IF NOT EXISTS Material (
  material_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNQIUE,
  group_name TEXT NOT NULL
);

-- Sample Table: Represents biological replicates for each material condition (39 samples total)
CREATE TABLE IF NOT EXISTS Sample (
  sample_id TEXT PRIMARY KEY,
  material_id INTEGER NOT NULL,
  replicate_number INTEGER NOT NULL,
  FOREIGN KEY (material_id) REFERENCES Material(material_id)
);

-- Gene Table: Focused immune response gene panel
CREATE TABLE IF NOT EXISTS Gene (
  gene_id TEXT PRIMARY KEY,
  symbol TEXT NOT NULL,
  immune_response_category TEXT NOT NULL
);

-- ExpressionMeasurement Table: Processed normalized expression values
CREATE TABLE IF NOT EXISTS ExpressionMeasurement (
  measurement_id INTEGER PRIMARY KEY AUTOINCREMENT,
  sample_id TEXT NOT NULL,
  gene_id TEXT NOT NULL,
  processed_expression_value REAL NOT NULL,
  FOREIGN KEY (sample_id) REFERENCES Sample(sample_id),
  FOREIGN KEY (gene_id) REFERENCES Gene(gene_id)
);
