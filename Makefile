extract-assets:
	python main.py extractor extract-assets

extract-texts:
	python main.py extractor extract-texts

reimport-texts:
	python main.py reimport reimport-texts

gpt-translate:
	python main.py translator chatgpt-translate

update:
	python main.py manager update --local

install:
	python main.py manager install

uninstall:
	python main.py manager uninstall
