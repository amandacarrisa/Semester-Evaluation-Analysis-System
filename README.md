(Original repo in description)

Employed Django framework to develop an advanced university evaluation system featuring customized graphs and file parsing capabilities. Took responsibility for web design, model creation, and database maintenance throughout the project.



# EDOM-NG Backend

[![pipeline status](https://gitlab.com/semoga-ppl-a/edom-backend/badges/main/pipeline.svg)](https://gitlab.cs.ui.ac.id/semoga-ppl-a/edom-backend/-/commits/main) [![coverage report](https://gitlab.com/semoga-ppl-a/edom-backend/badges/main/coverage.svg)](https://gitlab.ui.ac.id/semoga-ppl-a/edom-backend/-/commits/main)

Repository for the Backend of EDOM-NG

## Changelogs

### 2022-03-06: Release 1
> Deployed on [our staging server](http://staging.edom-ng.franciswibisono.com/api)<br>
> Preview on the production server can be requested, but currently unavailable due to cost reasons
- Project initialization
- Project Dockerization
- CI/CD
- Database models
    - Base User
    - Professor
    - Mahasiswa
    - Admin
- REST API skeleton
- JWT skeleton
- Pre-Commit
- Sonarqube Integration
- Admin form

## Development

### Package Management and Virtual Environment

This repository uses `Pipenv` for virtual environment and package management. Make sure to read the [docs](https://pipenv.pypa.io/en/latest/) before setting up the project.

```
pip install --user pipenv
```

For more detailed information about installing Pipenv, refer to [this](https://pipenv.pypa.io/en/latest/install/#installing-pipenv).

#### To install dependencies

```
pipenv install
```

#### To install new dependecy

```
pipenv install <library_name>
```

#### To activate the virtual environment

```
pipenv shell
```

Alternatively, you can run a command inside the virtualenv with `pipenv run`. For example:

```
pipenv run python manage.py runserver
```

#### To add environment variables

Create new `.env` file in the same directory with Pipfile. Pipenv will automatically loads the variable when the shell is activated.

### Git hooks using pre-commit

The first thing you should do after cloning this repository and installing dependencies is to install pre-commit hooks.

```
pipenv run pre-commit install
```

These hooks are useful for identifying simple issues before submission to code review and ensure the code quality.

### Testing with Docker
## Developing or build with Docker

To ease up development you can use docker to create the environment necessary. You changes made in code will be automatically changed in the docker container as well so you can just run a docker container and develop like you normally would.

It should be noted that you would need to have both `docker` and `docker-compose` installed on your machine.

### Docker commands

To ease up creating, cleaning, etc. there exist a Makefile that contains the commands that is used. Should you be unable to use it then you can simply copy the command in the Makefile.

#### Start container

```
make up
```

#### Kill container

```
make kill
```

#### Build docker image

```
make build
```

#### Make migrations

```
make make_migration
```

#### Migrate

```
make migrate
```

#### Clean volumes or creates files

```
make clean
```
