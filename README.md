# The Wall task

### Configiration:

  - config.py `MULTIPROCESING_MODE` - True or False. If the flag is True the building of the wall happens using more than 1 process. Otherwise, normal run.
  - config.py `PROCESSES` - How many process we will alocate for the multiprocessing mode.
  - input_data.txt - We can configurate our input in this file.

### How to run:

```
git clone git@github.com:YovchoGandjurov/the-wall-task.git
cd the-wall-task
python3 -m venv venv
python3 install -r requirements.txt
cd the_wall_api
python3 manage.py runserver
```

### Things that will be good to be added:
  - Unit tests