extract-assets:
	python main.py builder extract-assets

extract-texts:
	python main.py builder extract-texts

gpt-translate:
	python main.py builder translate

google-translate:
	python main.py builder translate --google

generate:
	python main.py builder generate

translation-folder:
	python main.py builder make-translation-folder

update:
	python main.py manager install

update-local:
	python main.py manager install --local

uninstall:
	python main.py manager uninstall

pack-gui:
	auto-py-to-exe
