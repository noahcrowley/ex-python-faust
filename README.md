# ex-python-faust
_Faust Exploration_

- [Examples](#examples)
  - [hello_world](#hello_world)
  - [page_views](#page_views)
- [Notes](#notes)

>[Faust](https://faust-streaming.github.io/) is a stream processing library, porting the ideas from Kafka Streams to Python.
>
>It is used at Robinhood to build high performance distributed systems and real-time data pipelines that process billions of events every day.

## Local Development

This repository uses [Pipenv](https://pipenv.pypa.io/en/latest/) for package managment & isolation.

Python version management using [asdf](https://asdf-vm.com/) is supported via [`/.tool-versions`](/.tool-versions).

All examples require [Kafka](https://kafka.apache.org/), container config is provided in [`/docker-compose.yaml`](/docker-compose.yaml). Start Kafka:

```
docker-compose up -d
```

## Examples

### hello_world

Run app:

```
faust -A hello_world worker -l info
```

Use `faust send` to send a message to the `greetings` topic:

```
faust -A hello_world send greetings "Hello Kafka"
```

### page_views

Run app:

```
faust -A page_views worker -l info
```

Use `kcat` to stream messages from `page_views-page_views-changelog`:

```
kcat -b localhost -t page_views-page_views-changelog -K :
```

`faust send` message to `page_views` topic:
```
faust -A page_views send page_views '{"id": "foo", "user": "bar"}'
```

## Notes
- Pypi package `faust-streaming` is a fork of the deprecated `faust`
- `print()` statements are categorized as the "warning" log level, seems weird
- Creates empty folders even when using `store='memory://'`, not sure why
- In "[App Instantiation and Configuration](https://faust-streaming.github.io/faust/userguide/application.html#id3)" it says:
  > Instantiating and setting the configurations of a Faust app can be done in two steps, much like a Flask app. One can create a new App instance with the entire configuration as parameters and then run it, or instantiate the App, set the parameters and then run the application. This allows for easier configuration switching (in particular during development and testing phases).
  
  What does the last sentence mean?
- 