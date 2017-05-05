FROM rhel:7
ENV TERM=dumb
ADD . /tmp/citywars
WORKDIR /tmp/citywars
CMD ["python","main.py"]
