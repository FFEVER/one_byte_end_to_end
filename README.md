# One Byte End to End - Distributed Computing KMITL

This README would normally document whatever steps are necessary to get the
application up and running.

This is a **simple poll web application**. The goal of this repository is to demonstrate how the following tools can be linked together to create a continuous delivery and continuous integration development.

- Github
- Jenkins / Chef
- Selenium
- Autocannon / JMeter
- Dockers
- Kubernetes

Things you may want to cover:

- [One Byte End to End - Distributed Computing KMITL](#one-byte-end-to-end---distributed-computing-kmitl)
- [Python and Django Version](#python-and-django-version)
- [Database](#database)
- [Testing](#testing)
- [Up and Running](#up-and-running)
- [What does the app do?](#what-does-the-app-do)
  - [Create admin user](#create-admin-user)
  - [Login as admin](#login-as-admin)

To be updated

- Deployment instructions

# Python and Django Version

`python 3.7.6`

`django 3.0.3`

We use [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) as a Python version and environment manager.

Please follow the tutorials from their github repo to set it up if you want to run the development server directly from your computer.

# Database

`sqlite 3.31.1`

We use **sqlite** for simplification. If you use Mac, you can install it directly from **homebrew**.

```
$ brew install sqlite3
```

# Testing

You can run test suits from the root directory of the project with the following command:

```
$ python manage.py test polls
```

The test cases are implemented in `/polls/tests.py`.

# Up and Running

After cloning the repo and setup **python** and **django**, you can run the development server by the following command:
```
$ python manage.py runserver
```
Go to `localhost:8000/polls/` in your browser. You should see the text `"No polls are available."`.

# What does the app do?
The app the a simple poll app from the [official django tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/). It has the following functionalities:
- You can create polls with `question_text` and `pub_date` (date published).
- The poll can have many `choices`.
- You can select the `poll` and vote for `choices`.
- You can see the results of votes for every `choices`.

## Create admin user
Once you have run the server, you need to create a new admin user. Run the following command:
```
$ python manage.py createsuperuser
```

Enter your desired username and press enter.
```
Username: admin
```

You will then be prompted for your desired email address:
```
Email address: admin@example.com
```

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```
Password: **********
Password (again): *********
Superuser created successfully.
```

## Login as admin and add a poll

If the server is not running start it like so:
```
$ python manage.py runserver
```

Now, open a Web browser and go to “/admin/” on your local domain – e.g., `http://127.0.0.1:8000/admin/`. You should see the admin’s login screen. Enter you username and password as you have created and press `login`.

Now, you should see the section `POLLS` and `Questions` under it. Click the `+ Add` button located at the right side of `Questions` section.

Enter all the information (question text, date published, 3 choices) and click `SAVE` button at the buttom.

## Vote and see the results
After you have created a new poll from the admin panel. You can go to the poll **index** page (`http://127.0.0.1:8000/polls/`). You should see the created poll listed there. If not, check the publish date whether it is today or in the past or not because you should not see the poll that would be published in the future.

Then you can click on the poll and vote for the choices. After voted, the web should redirect you to the **results** page.
