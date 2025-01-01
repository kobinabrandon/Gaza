raw_data:
	poetry run python src/feature_pipeline/data_sourcing.py	

training_data:
	poetry run python src/feature_pipeline/data_processing.py	
