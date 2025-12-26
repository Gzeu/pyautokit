"""Data transformation and processing utilities."""

import argparse
import csv
import json
from pathlib import Path
from typing import List, Dict, Any, Callable, Optional
from .logger import setup_logger
from .config import Config
from .utils import load_json, save_json

logger = setup_logger("DataProcessor", level=Config.LOG_LEVEL)


class DataProcessor:
    """Process and transform data from various formats."""

    def __init__(self):
        """Initialize data processor."""
        pass

    def load_csv(
        self,
        file_path: Path,
        delimiter: str = ",",
        encoding: str = "utf-8"
    ) -> List[Dict[str, str]]:
        """Load CSV file to list of dicts.
        
        Args:
            file_path: Path to CSV file
            delimiter: CSV delimiter
            encoding: File encoding
            
        Returns:
            List of row dicts
        """
        data = []
        try:
            with open(file_path, "r", encoding=encoding, newline="") as f:
                reader = csv.DictReader(f, delimiter=delimiter)
                data = list(reader)
            logger.info(f"Loaded {len(data)} rows from {file_path}")
        except Exception as e:
            logger.error(f"Failed to load CSV: {e}")
        return data

    def save_csv(
        self,
        data: List[Dict[str, Any]],
        file_path: Path,
        delimiter: str = ",",
        encoding: str = "utf-8"
    ) -> bool:
        """Save data to CSV file.
        
        Args:
            data: List of row dicts
            file_path: Output file path
            delimiter: CSV delimiter
            encoding: File encoding
            
        Returns:
            True if successful
        """
        if not data:
            logger.warning("No data to save")
            return False
        
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, "w", encoding=encoding, newline="") as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=delimiter)
                writer.writeheader()
                writer.writerows(data)
            logger.info(f"Saved {len(data)} rows to {file_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to save CSV: {e}")
            return False

    def filter_data(
        self,
        data: List[Dict],
        condition: Callable[[Dict], bool]
    ) -> List[Dict]:
        """Filter data based on condition.
        
        Args:
            data: Input data
            condition: Filter function
            
        Returns:
            Filtered data
        """
        filtered = [row for row in data if condition(row)]
        logger.info(f"Filtered {len(data)} rows to {len(filtered)} rows")
        return filtered

    def transform_data(
        self,
        data: List[Dict],
        transformer: Callable[[Dict], Dict]
    ) -> List[Dict]:
        """Transform data with function.
        
        Args:
            data: Input data
            transformer: Transform function
            
        Returns:
            Transformed data
        """
        transformed = [transformer(row) for row in data]
        logger.info(f"Transformed {len(data)} rows")
        return transformed

    def aggregate_data(
        self,
        data: List[Dict],
        group_by: str,
        agg_fields: Dict[str, str]
    ) -> List[Dict]:
        """Aggregate data by field.
        
        Args:
            data: Input data
            group_by: Field to group by
            agg_fields: Dict of {field: operation} (sum, count, avg, min, max)
            
        Returns:
            Aggregated data
        """
        from collections import defaultdict
        
        groups = defaultdict(lambda: defaultdict(list))
        
        for row in data:
            key = row.get(group_by)
            if key is None:
                continue
            
            for field in agg_fields.keys():
                if field in row:
                    try:
                        groups[key][field].append(float(row[field]))
                    except ValueError:
                        continue
        
        results = []
        for key, fields in groups.items():
            result = {group_by: key}
            
            for field, operation in agg_fields.items():
                values = fields.get(field, [])
                if not values:
                    continue
                
                if operation == "sum":
                    result[f"{field}_sum"] = sum(values)
                elif operation == "count":
                    result[f"{field}_count"] = len(values)
                elif operation == "avg":
                    result[f"{field}_avg"] = sum(values) / len(values)
                elif operation == "min":
                    result[f"{field}_min"] = min(values)
                elif operation == "max":
                    result[f"{field}_max"] = max(values)
            
            results.append(result)
        
        logger.info(f"Aggregated into {len(results)} groups")
        return results

    def convert_csv_to_json(
        self,
        csv_path: Path,
        json_path: Path
    ) -> bool:
        """Convert CSV to JSON.
        
        Args:
            csv_path: Input CSV path
            json_path: Output JSON path
            
        Returns:
            True if successful
        """
        data = self.load_csv(csv_path)
        if data:
            save_json(data, json_path)
            return True
        return False

    def convert_json_to_csv(
        self,
        json_path: Path,
        csv_path: Path
    ) -> bool:
        """Convert JSON to CSV.
        
        Args:
            json_path: Input JSON path
            csv_path: Output CSV path
            
        Returns:
            True if successful
        """
        data = load_json(json_path)
        if isinstance(data, list) and data:
            return self.save_csv(data, csv_path)
        logger.error("JSON data must be a non-empty list of dicts")
        return False

    def deduplicate(
        self,
        data: List[Dict],
        key_fields: List[str]
    ) -> List[Dict]:
        """Remove duplicate rows based on key fields.
        
        Args:
            data: Input data
            key_fields: Fields to use for uniqueness
            
        Returns:
            Deduplicated data
        """
        seen = set()
        unique = []
        
        for row in data:
            key = tuple(row.get(field) for field in key_fields)
            if key not in seen:
                seen.add(key)
                unique.append(row)
        
        logger.info(f"Removed {len(data) - len(unique)} duplicates")
        return unique


def main() -> None:
    """CLI for data processor."""
    parser = argparse.ArgumentParser(description="Data processing utility")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Convert CSV to JSON
    csv2json = subparsers.add_parser("csv2json", help="Convert CSV to JSON")
    csv2json.add_argument("input", help="Input CSV file")
    csv2json.add_argument("output", help="Output JSON file")
    
    # Convert JSON to CSV
    json2csv = subparsers.add_parser("json2csv", help="Convert JSON to CSV")
    json2csv.add_argument("input", help="Input JSON file")
    json2csv.add_argument("output", help="Output CSV file")
    
    # Filter data
    filter_parser = subparsers.add_parser("filter", help="Filter CSV data")
    filter_parser.add_argument("input", help="Input CSV file")
    filter_parser.add_argument("output", help="Output CSV file")
    filter_parser.add_argument("--field", required=True, help="Field to filter")
    filter_parser.add_argument("--value", required=True, help="Value to match")
    
    args = parser.parse_args()
    processor = DataProcessor()
    
    if args.command == "csv2json":
        processor.convert_csv_to_json(Path(args.input), Path(args.output))
    elif args.command == "json2csv":
        processor.convert_json_to_csv(Path(args.input), Path(args.output))
    elif args.command == "filter":
        data = processor.load_csv(Path(args.input))
        filtered = processor.filter_data(
            data,
            lambda row: row.get(args.field) == args.value
        )
        processor.save_csv(filtered, Path(args.output))


if __name__ == "__main__":
    main()