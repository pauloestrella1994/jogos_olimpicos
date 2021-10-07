# Olympic Games

An API that provides data for two differents sports: Swimming and Dar Throw.

In this API, you can add data from athletes and competitions and then return in a
partial podium or final podium

This API uses [Python](https://www.python.org/about/), [Django](https://www.djangoproject.com/), [Django Rest Framework](https://www.django-rest-framework.org/), [PostresSQL](https://www.postgresql.org/) and [Docker](https://www.docker.com/). If you have any doubts, make sure you acess their documentation

## Swimming
For the swimming competition, you can GET, POST, PATCH and DELETE data, considering the id lookup field, in both of urls (localhost):

```
http://localhost:8000/swimming-athletes/
http://localhost:8000/swimming-competition/
```
Example of a payload for the swimming athletes url:

```
  {
    "id": 1,
    "competition": 1,
    "athlete": "Cesar Cielo",
    "value": "10.235",
    "unit_measurement": "s"
  }
```

Example of a payload for the swimming competition url:

```
  {
    "id": 1,
    "competition_name": "100m classificatoria 1",
    "start_date": "2021-09-04",
    "end_date": null,
    "results": "partial_result",
    "athletes_results": [
      {
        "id": 2,
        "competition": 1,
        "athlete": "Michael Phelps",
        "value": "9.235",
        "unit_measurement": "s"
      },
      {
        "id": 1,
        "competition": 1,
        "athlete": "Cesar Cielo",
        "value": "10.235",
        "unit_measurement": "s"
      }
    ]
  }
```

In the swimming competition, if you send an update with end_date field (using PATCH HTTP verb, for example), you automatically transform results from partial to ended competition. The podium is shown by the ordering of nested alhletes in competition url.

#### Constraints
- Does not support competition with start and end date in the same POST;
- Does not support two or more marks of the same athlete in the same competition;
- Does not support competition with end_date before than start_date;
- Does not support more athletes in competitions that has been ended.

## Dart Throw
For the dart throw competition, you can GET, POST, PATCH and DELETE data, considering the id lookup field, in all urls (localhost):

```
http://localhost:8000/dart-throw-athletes/
http://localhost:8000/dart-throw-competition/
http://localhost:8000/dart-throw-podium/<competition_id>/
```

Example of a payload for the dart throw athletes url:

```
  {
    "id": 1,
    "competition": 1,
    "athlete": "Joao dos dardos",
    "value": "80.235",
    "unit_measurement": "m"
  }
```

Example of a payload for the dart throw competition url:

```
   {
    "id": 1,
    "competition_name": "Dardo semifinal",
    "start_date": "2021-09-04",
    "end_date": null,
    "results": "partial_result",
    "athletes_results": [
      {
        "id": 4,
        "competition": 1,
        "athlete": "Michael dos dardos",
        "value": "100.235",
        "unit_measurement": "m"
      },
      {
        "id": 3,
        "competition": 1,
        "athlete": "Michael dos dardos",
        "value": "90.235",
        "unit_measurement": "s"
    }
```

Example of a payload for the dart throw podium url:

```
[
  {
    "athlete": "Michael dos dardos",
    "value": "100.235",
    "unit_measurement": "m"
  },
  {
    "athlete": "Joao dos dardos",
    "value": "80.235",
    "unit_measurement": "m"
  }
]
```

In the dart competition, if you send an update with end_date field (using PATCH HTTP verb, for example), you automatically transform results from partial to ended competition. The podium is shown by the ordering alhletes in dart-throw-podium url, make sure you add in url, the id of the competition you want to see the parcial or final result. Also, in competition url you can get the marks of the all athletes, nested in their respective competitions.

#### Constraints
- Does not support competition with start and end date in the same POST;
- Does not support more then three marks of the same athlete in the same competition;
- Does not support competition with end_date before than start_date;
- Does not support more athletes in competitions that has been ended.


# Installation

Before you start, make sure you have [Docker](https://docs.docker.com/engine/install/) and [Docker-Compose](https://docs.docker.com/compose/install/) installed.

Copy the template `local.env` and add your secret key to django settings in `.env`:

```
cp local.env .env
SECRET_KEY=YourSecretKey
```

To run and build the project*:

```
docker-compose up --build
```

To execute the migrate to PostgreSQL database:
```
docker-compose run web python manage.py migrate
```

If you want to load some data to start use your API, run the following commands. Make sure you are running in the same sequence below, just to avoid problems with database tables relationships:

```
docker-compose run web python manage.py loaddata dartthrow_competition.json
docker-compose run web python manage.py loaddata dartthrow_athletes.json
docker-compose run web python manage.py loaddata swimming_competition.json
docker-compose run web python manage.py loaddata swimming_athletes.json
```

Thats all folks, enjoy it!

PS*: If you have any trouble to run the commands above, make sure you run with `sudo`.
