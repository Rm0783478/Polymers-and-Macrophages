-- Analytical SQL Queries for Biomaterial Transcriptomics
-- Author: Rohan Mishra

-- Query: Calculate mean expression of immune response genes grouped by material property group
SELECT
    m.group_name
    g.symbol AS gene_symbol
    ROUND(AVG(e.processed_expression_value), 3) AS mean_expression
FROM ExpressionMeasurement e
JOIN Sample s ON e.sample_id = s.sample_id
JOIN Material m ON s.material = m.material_id
JOIN Gene g ON e.gene_id = g.gene_id
GROUP BY m.group_name, g.symbol
ORDER BY m.group_name, mean_expression DESC;
