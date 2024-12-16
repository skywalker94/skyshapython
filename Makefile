setup:
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*

publish: setup upload

test:
	pytest tests/

heap-test:
	pytest tests/test_max_heaps.py
	pytest tests/test_min_heaps.py

sort-test:
	pytest tests/test_sort_master.py