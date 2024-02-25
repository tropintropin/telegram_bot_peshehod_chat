.PHONY: all \
	check-user \
	install-redis run-redis \
	install-sqlite \
	install-venv install-requirements \
	create-symlink reload-systemd enable-service start-service check-service \
	check-redis check-sqlite

# Setup variables
SERVICE_PATH := $$(pwd)/setup/telegram-bot-peshehod.service

# Check python3 and pip3
PYTHON3_OK := $(shell command -v python3)
PIP3_OK := $(shell command -v pip3)

ifeq ('$(PYTHON3_OK)','')
	$(error Python 3 is not installed. Please install Python 3.)
endif

ifeq ('$(PIP3_OK)','')
	$(error pip3 is not installed. Please install pip3.)
endif

all: check-user install-redis run-redis install-sqlite \
	install-venv install-requirements \
	create-symlink reload-systemd enable-service start-service check-service

# Check user peshehod
check-user:
	@if ! id -u peshehod > /dev/null 2>&1; then \
		echo "User peshehod does not exist. Creating..."; \
		sudo useradd -r -s /usr/sbin/nologin peshehod; \
	else \
		echo "User peshehod already exists."; \
	fi

# Check and install Redis
check-redis:
	@if ! command -v redis-server > /dev/null 2>&1; then \
		make install-redis; \
	else \
		echo "Redis is already installed."; \
	fi

install-redis:
	sudo apt update
	sudo apt install -y redis-server

run-redis:
	sudo service redis-server restart
	redis-cli ping

# Check and install SQLite
check-sqlite:
	@if ! command -v sqlite3 > /dev/null 2>&1; then \
		make install-sqlite; \
	else \
		echo "SQLite is already installed."; \
	fi

install-sqlite:
	sudo apt update
	sudo apt install -y sqlite3
	sqlite3 --version

# Telegram bot setup
install-venv:
	@if [ ! -d "venv" ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv venv; \
	else \
		echo "Virtual environment already exists."; \
	fi

install-requirements:
	. venv/bin/activate && pip3 install -r requirements.txt

create-symlink:
	sudo ln -sf $(SERVICE_PATH) /etc/systemd/system/telegram-bot-peshehod.service

reload-systemd:
	sudo systemctl daemon-reload

enable-service:
	sudo systemctl enable telegram-bot-peshehod.service

start-service:
	sudo systemctl start telegram-bot-peshehod.service

check-service:
	sudo systemctl --no-pager status telegram-bot-peshehod.service
	echo "Checking if service is active..."
	sudo systemctl --no-pager is-active telegram-bot-peshehod.service
