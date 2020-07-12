# Accionlabs-Task
Blog post which determines the palindrome property and allows users to perform CRUD operations

This task is developed using Django and Django-Rest-Framework.

Allowd Urls: 
  Local: localhost:8000 (or) 127.0.0.1:8000    [Make sure to change the allowed hosts in settings.py file of mywebsite]
  
  Production: https://accionlabs-vijay.herokuapp.com

This project is deployed to heroku platform using Dockerfile.

Steps followed :
  1) heroku create  appname(eg: accionlabs-vijay)
  2) heroku config:set SECRET_KEY=SOME_SECRET_VALUE -a accionlabs-vijay
  3) ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'accionlabs-vijay.herokuapp.com']

Following the Build Manifest file:
  Heroku builds and deploys Docker images based on a heroku.yml manifest file.
  
  4) heroku update beta
  5) heroku plugins:install @heroku-cli/plugin-manifest
With that, initialize a Git repo and create a commit.
Then, add the Heroku remote:
   heroku git:remote -a accionlabs-vijay.herokuapp.com
  
 git push heroku master
 
 
 Verify https://accionlabs-vijay.herokuapp.com/   -->This works..
 



