from pathlib import Path
import json
from .validators import validate_schema, validate_required_fields, validate_unique_keys, report_duplicate_rows, validate_allowed_values, validate_numeric_range, validate_referential_integrity
from .schemas import EXPECTED_SCHEMAS, REQUIRED_COLUMNS, UNIQUE_KEYS, ALLOWED_VALUES, NUMERIC_RANGE, REFERENTIAL_INTEGRITY
from .data_loader import load_datasets

root = Path(__file__).parents[1]

validation_report_path = root / "reports" / "validation_report.json"

def record_validation_result(validation_results, dataset, check, status, message):
    validation_result={}
    validation_result['dataset'] = dataset
    validation_result['check'] = check
    validation_result['status'] = status
    validation_result['message'] = message

    validation_results.append(validation_result)

def main():
    loaded_dataframes = load_datasets()
    dataframes={}

    validation_results=[]   

    #validating dataset
    expected_datasets = set(EXPECTED_SCHEMAS.keys())
    datasets = loaded_dataframes.keys()
    actual_datasets = set(datasets)
    missing_datasets = expected_datasets - actual_datasets

    if missing_datasets:
        for missing_dataset in missing_datasets:
            record_validation_result(validation_results, missing_dataset, "dataset_availability", "FAILED", "The expected CSV file is missing from the raw data directory.")

    # Loading
    for filename, df in loaded_dataframes.items():

        if filename in EXPECTED_SCHEMAS:
            dataframes[filename] = df

        else:
            print(f"Schema not defined for {filename}")

    # Validation
    for filename, df in dataframes.items():

        # Schema Validation
        expected_cols = EXPECTED_SCHEMAS[filename]
        actual_cols = set(df.columns)
    
        schema_valid = True

        try:
            validate_schema(expected_cols, actual_cols)
            print(f"Schema validation passed: {filename}")
            record_validation_result(validation_results, filename, "schema_validation", "PASSED", "All expected columns are present")

        except ValueError as error:
            schema_valid = False
            print(f"Schema validation failed: {filename} - {error}")
            record_validation_result(validation_results, filename, "schema_validation", "FAILED", f"Schema validation failed: {filename} - {error}")

        if schema_valid:

            # Required column validation

            if filename in REQUIRED_COLUMNS:
                required_cols = REQUIRED_COLUMNS[filename]

                try:
                    validate_required_fields(df, required_cols)
                    print(f"Required column validation passed: {filename}")
                    record_validation_result(validation_results, filename, "required_fields", "PASSED", "All required fields contain values")

                except ValueError as error:
                    print(f"Required column validation failed: {filename} - {error}")
                    record_validation_result(validation_results, filename, "required_fields", "FAILED", f"Required column validation failed: {filename} - {error}")

            else:
                print(f"Required column not defined for {filename}")
                record_validation_result(validation_results, filename, "required_fields", "NOT_CONFIGURED", f"No required columns defined for {filename}")

            # Unique keys validation

            if filename in UNIQUE_KEYS:
                unique_keys = UNIQUE_KEYS[filename]

                try:
                    validate_unique_keys(df, unique_keys)
                    print(f"Unique keys validation passed for {filename}")
                    record_validation_result(validation_results, filename, "unique_keys", "PASSED", "No duplicate key combinations found")

                except ValueError as error:
                    print(f"Unique keys validation failed for {filename} - {error}")
                    record_validation_result(validation_results, filename, "unique_keys", "FAILED", f"Unique keys validation failed for {filename} - {error}")

            else:
                print(f"Unique keys not defined for {filename}")
                record_validation_result(validation_results, filename, "unique_keys", "NOT_CONFIGURED", f"No unique keys defined for {filename}")

            # Duplicate report

            duplicate_count = report_duplicate_rows(df)
            if duplicate_count:
                print(f"Exact duplicate rows detected: {duplicate_count}")
                record_validation_result(validation_results, filename, "exact_duplicates", "FAILED", f"Duplicate rows found for {filename} - {duplicate_count}")
            else:
                print(f"No exact duplicate rows detected")
                record_validation_result(validation_results, filename, "exact_duplicates", "PASSED", f"No exact duplicate rows detected for {filename}")

            # Allowed values
        
            if filename in ALLOWED_VALUES:
                allowed_values = ALLOWED_VALUES[filename]
                try:
                    for column, values in allowed_values.items():
                        validate_allowed_values(df[column], column, values)
                    print(f"Allowed values validation passed: {filename}")
                    record_validation_result(validation_results, filename, "allowed_values", "PASSED", "All allowed values are present")
                except ValueError as error:
                    print(f"Allowed values validation failed: {filename} - {error}")
                    record_validation_result(validation_results, filename, "allowed_values", "FAILED", f"Allowed values validation failed: {filename} - {error}")
            else:
                print(f"No allowed values for {filename}")
                record_validation_result(validation_results, filename, "allowed_values", "NOT_CONFIGURED", f"No allowed values defined for {filename}")

            # Numeric value validation
        
            if filename in NUMERIC_RANGE:
                numeric_range = NUMERIC_RANGE[filename]
                try:
                    for column, n_range in numeric_range.items():
                        validate_numeric_range(df[column], column, n_range['minimum'], n_range['maximum'])
                    print(f"Numeric range validation passed: {filename}")
                    record_validation_result(validation_results, filename, "numeric_range", "PASSED", "All values are within the configured numeric ranges")
                except ValueError as error:
                    print(f"Numeric range validation failed: {filename} - {error}")
                    record_validation_result(validation_results, filename, "numeric_range", "FAILED", f"Numeric range validation failed: {filename} - {error}")
            else:
                print(f"No numeric range for: {filename}")
                record_validation_result(validation_results, filename, "numeric_range", "NOT_CONFIGURED", f"No numeric range defined for {filename}")

            # Referential Integrity validation

            if filename in REFERENTIAL_INTEGRITY:
                rules = REFERENTIAL_INTEGRITY[filename]
                if rules["parent_dataset"] in dataframes.keys():

                    parent_dataset = dataframes[rules["parent_dataset"]]
                    child_column = rules["child_column"]
                    child_series = df[child_column]
                    parent_column = rules["parent_column"]
                    parent_series = parent_dataset[parent_column]

                    try:
                        validate_referential_integrity(child_series, parent_series)
                        print(f"Referential integrity validation passed: {filename}")
                        record_validation_result(validation_results, filename, "referential_integrity", "PASSED", "All child references exist in the parent dataset")

                    except ValueError as error:
                        print(f"Referential integrity validation failed: {filename} - {error}")
                        record_validation_result(validation_results, filename, "referential_integrity", "FAILED", f"Referential integrity validation failed: {filename} - {error}")

                else:
                    print(f"Parent dataset is not present for {filename}")
                    record_validation_result(validation_results, filename, "referential_integrity", "SKIPPED", f"Parent dataset is not present for {filename}")

            else:
                print(f"No referential integrity for: {filename}")
                record_validation_result(validation_results, filename, "referential_integrity", "NOT_CONFIGURED", f"No referential integrity rules defined for {filename}")


    passed_count = len([i for i in validation_results if i['status'] == 'PASSED'])

    failed_count = len([i for i in validation_results if i['status'] == 'FAILED'])

    skipped_count = len([i for i in validation_results if i['status'] == 'SKIPPED'])

    not_configured_count = len([i for i in validation_results if i['status'] == 'NOT_CONFIGURED'])

    print('='*10 + "VALIDATION SUMMARY" + '='*10)
    print(f"Total checks: {len(validation_results)}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print(f"Skipped: {skipped_count}")
    print(f"Not Configured: {not_configured_count}")
    print('='*40)

    validation_report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(validation_report_path, 'w') as file:
        json.dump(validation_results, file, indent=4)

if __name__ == "__main__":
    main()