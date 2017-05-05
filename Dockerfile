FROM rhel7
ENV TERM=dumb
ADD citywars /tmp/citywars
WORKDIR /tmp/citywars
CMD ["python","main.py"]
