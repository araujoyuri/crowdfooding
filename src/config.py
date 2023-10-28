# import logging
import os

# import structlog
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	DB_HOST: str = os.getenv("DB_HOST", "postgres")
	DB_PASSWORD: str = os.getenv("DB_PASSWORD", "postgres")
	DB_NAME: str = os.getenv("DB_NAME", "crowdfooding")
	PYTHON_ENV: str = os.getenv("PYTHON_ENV", "local")


settings = Settings()

LOGGING_HANDLERS = ["console"] if settings.PYTHON_ENV == "local" else ["json"]
LOGGING = {
	"version": 1,
	"disable_existing_loggers": False,
	"formatters": {
		"default": {
			"format": "%(asctime)s:%(name)s:%(process)d:%(lineno)d %(levelname)s %(message)s"
		},
		"json": {
			"()": "pythonjsonlogger.jsonlogger.JsonFormatter",
			"format": """
                asctime: %(asctime)s
                created: %(created)f
                filename: %(filename)s
                funcName: %(funcName)s
                levelname: %(levelname)s
                levelno: %(levelno)s
                lineno: %(lineno)d
                message: %(message)s
                module: %(module)s
                msec: %(msecs)d
                name: %(name)s
                pathname: %(pathname)s
                process: %(process)d
                processName: %(processName)s
                relativeCreated: %(relativeCreated)d
                thread: %(thread)d
                threadName: %(threadName)s
                exc_info: %(exc_info)s
            """,
			"datefmt": "%Y-%m-%d %H:%M:%S",
		},
	},
	"handlers": {
		"console": {
			"class": "logging.StreamHandler",
			"stream": "ext://sys.stdout",
			"formatter": "default",
		},
		"json": {
			"class": "logging.StreamHandler",
			"formatter": "json",
		},
	},
	"loggers": {
		"uvicorn": {"level": "CRITICAL"},
		"urllib3": {
			"level": "CRITICAL",
		},
		"asyncio": {
			"level": "WARNING",
		},
	},
	"root": {"level": "INFO", "handlers": LOGGING_HANDLERS},
}


# TODO: fix structlog configuration
# structlog.configure(
# 	processors=[
# 		structlog.contextvars.merge_contextvars,
# 		structlog.processors.add_log_level,
# 		structlog.processors.StackInfoRenderer(),
# 		structlog.dev.set_exc_info,
# 		structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S", utc=True),
# 		structlog.dev.ConsoleRenderer(),
# 	],
# 	wrapper_class=structlog.make_filtering_bound_logger(logging.NOTSET),
# 	context_class=dict,
# 	logger_factory=structlog.PrintLoggerFactory(),
# 	cache_logger_on_first_use=False,
# )
