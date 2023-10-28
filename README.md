# CrowdFooding

## Table of Contents
1. [Introduction](#introduction)
2. [How It Works](#how-it-works)
3. [App Overview](#app-overview)
4. [Technical Details](#technical-details)
5. [Getting Started](#getting-started)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

### Overview
CrowdFooding is a personal software engineering project that aims to make a positive impact on the lives of people 
dealing with food insecurity. The project's core idea is to create a non-profit food delivery system that provides an 
alternative to major apps with exploitative fees. It's my way of contributing to the community and helping those in 
need.

## How It Works

### User Donations
CrowdFooding encourages users to round up their orders and donate the extra cents to support the operation of the app. 
It's a small yet meaningful way to help those in need while enjoying the convenience of food delivery.

### Future Expansion
In the future, we plan to allow sellers to advertise their products in a more prominent area of the app. We understand 
that this vision is ambitious, but we're committed to making it a reality and creating a positive impact on the world.

## App Overview

### Architecture
The CrowdFooding app is designed with a three-part architecture:

1. 🖥️ **Frontend**: A simple UI that provides users with easy navigation.
2. 🌐 **REST API**: Initially, the API will serve as a Backend-For-Frontend (BFF). We have plans to transition to a 
GraphQL API in the future.
3. 🚀 **Worker**: Runs on top of Kafka to handle asynchronous tasks.

We anticipate the need for a restaurant manager back office in the future, but this will be addressed in subsequent 
phases.

## Technical Details

### Technology Stack
- 🐍 **Python**: The primary language for the backend.
- ⚡ **FastAPI**: The web framework of choice.
- 📝 **Pydantic**: For data validation.
- 🪶 **Structlog**: The structured logging library.
- 🛢️ **SQLAlchemy**: The ORM (with consideration for switching to SQLModel).
- 🛠️ **Alembic**: The migrations manager.
- 🐘 **Postgres**: The persistent storage solution.
- 🐳 **Docker**: Container image deployment.
- 🐳 **Docker Compose**: Local container orchestration.
- 📏 **Ruff**: The linter and formatter.
- 🚀 **Uvicorn**: The web server.

## Getting Started

### Prerequisites
- Docker and Docker Compose installed on your machine.
- Create a `.env` file following the `.env.example` file.

### Applying Migrations
To apply the migrations, use the following command:
```shell
make migrate_up
```

To revert to a previous migration, use:
```shell
make migrate_down
```

## Running the App
To run the CrowdFooding app, follow these steps:

### Prerequisites:
- Ensure you have Docker and Docker Compose installed on your machine.
- Create a `.env` file in the project's root directory, following the structure of the `.env.example` file.

### Starting the App:
To start the app, run the following command:

```shell
docker-compose up
```
This command will launch all the components of the app. At this stage, it includes the draft of the REST API.

### Stopping the App:
To stop the app, run the following command:
```shell
docker-compose down
```
If you wish to remove the volumes and orphan containers, you can add the following flags: `-v --remove-orphans`. This is 
particularly useful if you want to remove the volumes associated with the Postgres service.

### Running the App Outside Docker Compose:
If you prefer to run the app outside of Docker Compose, you can execute:
```shell
make run_dev
```
PS.: Before using the make commands, don't forget to `source .env`.

Now, you can run and test the CrowdFooding app on your local environment.

## Contributing
We welcome contributions to make CrowdFooding even better. Feel free to submit pull requests, report issues, or provide
suggestions.

## License
This project is licensed under the GNU General Public License 3.0 (GPL-3.0). Feel free to use and modify it as needed 
while adhering to the terms of the GPL-3.0.