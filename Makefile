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

install:
	python main.py manager install

update:
	python main.py manager install --update

force-update:
	python main.py manager install --update --force

uninstall:
	python main.py manager uninstall

pack-gui:
	auto-py-to-exe
