FROM gcc:latest

COPY main.cpp /usr/src/cpp_test

WORKDIR /usr/src/cpp_test

RUN g++ -o Test main.cpp

CMD ["./Test"]

