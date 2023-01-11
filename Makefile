#################################################################################
#
# Makefile to build the project
#
#################################################################################

PROJECT_NAME = de-py-katas
REGION = eu-west-2
PYTHON_INTERPRETER = python
WD=$(shell pwd)
PYTHONPATH=${WD}
SHELL := /bin/bash
PROFILE = default
PIP:=pip

# Define utility variable to help calling Python from the virtual environment
ACTIVATE_ENV := source venv/bin/activate

# Execute python related functionalities from within the project's environment
define execute_in_env
	$(ACTIVATE_ENV) && $1
endef

################################################################################################################
# Set Up
## Install flake8
flake:
	$(call execute_in_env, $(PIP) install flake8)

## Run the flake8 code check
run-flake:
	$(call execute_in_env, flake8 \
	./src/multiplication_table/*.py \
	./src/reduce_by_steps/*.py \
	./src/find_partner/*.py \
	./src/find_most_repeated/*.py \
	./src/vowel_shift/*.py \
	./src/alternating_split/*.py \
	./src/crack_code/*.py \
	./src/binary_search/*.py \
	./src/calculate_binary_score/*.py \
	./src/justify_line/*.py \
	./src/find_the_needle/*.py \
	./src/validate_suduko/*.py \
	./src/strange_sort/*.py \
	./src/gdpr_mask/*.py )
	
## Run the unit tests
unit-test:
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest -v)

## Run all checks
run-checks: run-flake unit-test