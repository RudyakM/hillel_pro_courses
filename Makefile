.PHONY check
check:
	black --check ./ && flake8 ./ && isort --chek-only ./

.PHONY fix
fix:
	black ./ && flake8 ./ && isort ./