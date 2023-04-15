extract-assets:
	python main.py extractor assets

extract-texts:
	python main.py extractor texts

reimport-texts:
	python main.py reimport texts

gpt-translate:
	python main.py translator chatgpt-translate

update:
	python main.py manager update --local

install:
	python main.py manager install

uninstall:
	python main.py manager uninstall

pack-gui:
	auto-py-to-exe
