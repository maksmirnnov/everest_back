git clone git@github.com:maksmirnnov/everest_front_typed.git
rm -r static/ && rm -r templates/everest_app/*
cp -r everest_front_typed/build ./
rm -r everest_front_typed
cp -r build/* templates/everest_app/
source ../bin/activate && python manage.py collectstatic
cp -r build/assets static/
service gunicorn restart
rm -r build/