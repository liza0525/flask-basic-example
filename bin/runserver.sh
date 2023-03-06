NUM_VCPUS=$(grep -c ^processor /proc/cpuinfo)

gunicorn -w $((NUM_VCPUS / 2)) -b "0.0.0.0:$1" app:app
