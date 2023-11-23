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

update:
	python main.py manager update

update-local:
	python main.py manager update --local

install:
	python main.py manager install

install-local:
	python main.py manager install --local

uninstall:
	python main.py manager uninstall

reimport-texts:
	python main.py reimport texts

pack-gui:
	auto-py-to-exe
