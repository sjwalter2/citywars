FROM centos:7
ENV TERM=dumb
ADD . /tmp/citywars
WORKDIR /tmp/citywars
CMD ["python3","main.py"]
