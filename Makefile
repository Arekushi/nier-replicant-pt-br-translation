start:
	python ./main.py

extract-assets:
	python -m src.commands.extractor extract-assets

extract-texts:
	python -m src.commands.extractor extract-texts

reimport-texts:
	python -m src.commands.reimport
